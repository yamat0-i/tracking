"""
Settings
"""
from pathlib import Path


# Path
root_dir = Path.cwd()
video_dir = root_dir / Path('video')  # Default: root/video
plots_dir = root_dir / Path('plots')  # Default: root/plots
log_dir = root_dir / Path('log')  # Default: root/log

videofilename = 'videofilename'

# Pixel size(in microns):
# umperpixel = 0.17768691284147112  # 40x
umperpixel = 0.7170625782472173  # 10x
# umperpixel = 1.4450851963350324  # 5x

# Plot range
select_plotrange_x = False  # Default: False
select_plotrange_y = False  # Default: False

xMin = 0
xMax = 15
yMin = 200
yMax = 800

# Thresholds of tracking
pMin = 0
pMax = 1000

# Activate linear fitting
fit = False  # Default: False

# Output file
output_t = True  # Default: True
output_y = False  # Default: False
output_dataM = False  # Default: False
output_t1 = True  # Default: True
output_y1 = True  # Default: True
output_posMax = True  # Default: True
