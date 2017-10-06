
import sys
import time

# Python Image Library
import Image

from naoqi import ALProxy



# http://doc.aldebaran.com/1-14/dev/python/examples/vision/get_image.html#python-example-vision-getimage
def showNaoImage(IP, PORT):

	camProxy = ALProxy("ALVideoDevice", IP, PORT)
	resolution = 2    # VGA
	colorSpace = 11   # RGB

	videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

	t0 = time.time()

	# Get a camera image.
	# image[6] contains the image data passed as an array of ASCII chars.
	naoImage = camProxy.getImageRemote(videoClient)

	t1 = time.time()

	# Time the image transfer.
	print "acquisition delay ", t1 - t0

	camProxy.unsubscribe(videoClient)


	# Now we work with the image returned and save it as a PNG  using ImageDraw
	# package.

	# Get the image size and pixel array.
	imageWidth = naoImage[0]
	imageHeight = naoImage[1]
	array = naoImage[6]

	# Create a PIL Image from our pixel array.
	im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

	# Save the image.
	im.save("camImage.png", "PNG")
	im.show()
