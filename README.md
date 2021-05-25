# rpi-timelapse

What it does:

Takes a picture every minute and add it to the /img directory


Instructions:

1. Create a /img and /video directory
2. Change the path in the cron.sh for the cronjob to execute properly
3. That's it.

you need to setup a cronjob to create the video:
0 0 * * * Pictures/timelapse/cron.sh  >/tmp/mycommand.log 2>&1 #change the path to the .sh

