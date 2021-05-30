#!/bin/bash

cd /
cd home/pi/Pictures/timelapse/
mv img/*.jpg video

cd video

ffmpeg -framerate 60 -pattern_type glob -i "img*.jpg" -s:v 1024x768 -c:v libx264 -crf 17 -pix_fmt yuv420p file.mp4 && mv file.mp4 file_`date +"%Y%m%d-%H%M%S"`.mp4 && rm *.jpg
