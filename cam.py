from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Camera settings
camera.rotation = 180
#camera.resolution = (2592, 1944) # Maximum resolution
#camera.resolution = (64,64) # Minimum res
#camera.framerate = 15 # must be 15 for max res

# Show a preview of what the camera sees
camera.start_preview()


# Capture an image (must sleep for 2+ seconds before
sleep(5)
camera.capture('image.jpg')

# Capture a video
#camera.start_recording('video.h264')
#sleep(5)
#camera.stop_recording()

# Stop the preview
camera.stop_preview()
