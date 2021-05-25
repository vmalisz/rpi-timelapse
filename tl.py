from time import sleep
import picamera
import glob
import os
from datetime import datetime
import shutil

def main():
	WAIT_TIME = 60

	now = datetime.now()
	timestamp = datetime.timestamp(now)
	timestamp = str(timestamp)

	imgdir = 'img'

	try:
		shutil.rmtree('/home/pi/Pictures/timelapse/'+imgdir+'/')
	except:
		print('no directory')

	with picamera.PiCamera() as camera:
		#camera.resolution = (1024, 768)
		#camera.resolution = (1296,972)
		#camera.resolution = (1024, 640)
		camera.resolution = (1207, 907)
		camera.rotation = 180
		#camera.awb_mode = 'horizon' #https://picamera.readthedocs.io/en/release-1.10/api_camera.html off/auto/sunlight/cloudy/shade/horizon
		#camera.annotate_text = "Hello world!"
		#camera.image_effect = "cartoon"
		os.mkdir(imgdir)

		for filename in camera.capture_continuous('/home/pi/Pictures/timelapse/'+imgdir+'/img_{timestamp:%Y%m%d_%H-%M-%S-%f}.jpg'):
			sleep(WAIT_TIME)
			#nbfiles = len(glob.glob(imgdir+'/*.jpg'))
			#print(f'NB FILES = {nbfiles}')
			#try:
				#oldestfile = sorted(glob.glob('/home/pi/Pictures/timelapse/'+imgdir+'/*.jpg'), key=os.path.getctime)[0]
				#if nbfiles > 800:
				#	os.remove(oldestfile)
			#except:
			#	continue
		# camera.start_preview()
		# while time_in_range(timestamp):
		# 	sleep(2)
		# 	camera.capture('/home/pi/Pictures/timelapse/'+imgdir+'/img_{timestamp:%Y%m%d_%H-%M-%S-%f}.jpg')



def time_in_range(x):
    """Return true if x is in the range [start, end]"""
    start =  datetime.time(5, 0, 0)
    end =  datetime.time(1, 0, 0)
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

if __name__ == '__main__':
    main()