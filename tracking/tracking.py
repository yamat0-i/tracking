from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt

import tracking.settings as settings


# Load settings
# Path
root_dir = settings.root_dir
video_dir = settings.video_dir
plots_dir = settings.plots_dir
videofilename = settings.videofilename
vedeofilepath = video_dir / Path(videofilename + '.avi')

# Pixel size(in microns):
umperpixel = settings.umperpixel

# Thresholds of brightness
pMin = settings.pMin
pMax = settings.pMax

# Plot range
sprx = settings.select_plotrange_x
spry = settings.select_plotrange_y
if sprx:
    xMin = settings.xMin
    xMax = settings.xMax
if spry:
    yMin = settings.yMin
    yMax = settings.yMax


def main():
    cap = cv2.VideoCapture(vedeofilepath)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    numFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    height, width, Y = set_tracking_parameters(cap=cap)
    if not Y:
        print("Error: No points were selected.")
        return
    
    t, y, dataM = read_data(
        cap=cap, numFrames=numFrames, width=width, fps=fps, Y=Y
        )

    # Plot
    plt.figure(0)
    plt.pcolor(range(numFrames), y/umperpixel, dataM)
    plt.ylabel("Position along fiber (pixels)")
    plt.xlabel("Frame #")
    plt.title('Unscaled')

    plt.figure(1)
    plt.pcolor(t, y, dataM, cmap="bone")
    if sprx:
        plt.xlim(xMin, xMax)
    if spry:
        plt.ylim(yMin, yMax)
    plt.ylabel("Position along fiber (um)")
    plt.xlabel("Time (s)")
    plt.title(videofilename)

    plt.show()


def set_tracking_parameters(cap):
    ret, img = cap.read()
    if ret == False:
        print('ret:', ret)
        exit(1) # debug
    clone = img.copy()
    height, width = img.shape[0], img.shape[1]
    cv2.imshow('image', img)
    Y = []

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            font = cv2.FONT_HERSHEY_COMPLEX
            Y.append(y)
            clone_img = clone.copy()
            cv2.putText(clone_img, str(x) + ', ' +
                            str(y), (x,y), font,
                            0.5, (255, 0, 0), 2)
            cv2.imshow('image', clone_img)
            print(f'Fiber located at y = {y} [px]')
            cv2.destroyWindow('image')

    print('Click on a particle')
    cv2.setMouseCallback('image', mouse_callback) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return height, width, Y


def read_data(cap, numFrames, width, fps, Y):
    # Parameters for measuring speed
    frameStart = 0
    frameFinish = numFrames
    Yf = Y[-1]
    # Variables for holding the data
    dataM = np.zeros((width, numFrames)) 
    t = np.arange(numFrames) / fps
    y = np.arange(width) * umperpixel
    posMax = np.zeros(numFrames)
    t1 = [] # These arrays will hold the times and positions of peaks in the data i.e. where the particle was found to be.
    y1 = []

    for frame in range(numFrames):
        ret, img = cap.read()
        if ret == False:
            break    
        fr = img[:,:,0]
        arr = fr[Yf,:]
        dataM[:,frame] = arr   
        posMaxArray = np.where(arr == np.amax(arr)) # find positions with max brightness
        elements0 = np.array(posMaxArray[0])
        elements = []
        for ii in range(elements0.size):
            if (elements0[ii]<=pMax) and (elements0[ii]>=pMin):
                elements.append(elements0[ii])
            else:
                continue
        mean = np.mean(elements)
        sd = np.std(elements, axis=0)
        pos_list = [x for x in elements if (x > mean - 2 * sd)]
        pos_list = [x for x in pos_list if (x < mean + 2 * sd)] # remove outliers using standard deviation
        posMax[frame] = np.mean(pos_list) * umperpixel
        if (frame in range(frameStart, frameFinish)) and not np.isnan(posMax[frame]):
            t1.append(frame / fps)
            y1.append(posMax[frame])

    cap.release()    
    t1 = np.array(t1)
    y1 = np.array(y1)
    return t, y, dataM
