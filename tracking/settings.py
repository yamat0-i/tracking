from pathlib import Path

### >>> Settings >>>

# Path
root_dir = Path.cwd()
video_dir = root_dir / Path('video') # Default
plots_dir = root_dir / Path('plots') # Default

videofilename = 'videofilename'

# Pixel size(in microns):
# umperpixel = 0.17768691284147112 #40x
umperpixel = 0.7170625782472173 #10x # Default
# umperpixel = 1.4450851963350324 #5x

# Thresholds of brightness
pMin = 400
pMax = 600

# Plot range
select_plotrange_x = False # Default: False
select_plotrange_y = False # Default: False

xMin = 0
xMax = 15
yMin = 0
yMax = 600

### <<< Settings <<<
