from pathlib import Path

### >>> Settings >>>

# Path
root_dir = Path.cwd()
video_dir = root_dir / Path('video') # Default
plots_dir = root_dir / Path('plots') # Default

videofilename = 'video_file_name'

# Pixel size(in microns):
# umperpixel = 0.17768691284147112 #40x
umperpixel = 0.7170625782472173 #10x # Default
# umperpixel = 1.4450851963350324 #5x

# Thresholds of brightness
pMin = 400
pMax = 600

# Plot region select (prs)
prs = False # Default: False
yMin = 200
yMax = 800

### <<< Settings <<<
