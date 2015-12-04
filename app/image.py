from base64 import decodestring

def save_image(image_encoded):
	fh = open("imageToSave.png", "wb")
	fh.write(image_encoded.decode('base64'))
	fh.close()