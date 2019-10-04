# USAGE
# python deep_learning_with_opencv.py --image images/jemma.png --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt

# import the necessary packages
import numpy as np
import argparse
import time
import cv2
import pytesseract

def label_detection(image_path):
	labels = './synset_words.txt'
	prototxt = './bvlc_googlenet.prototxt'
	model = './bvlc_googlenet.caffemodel'

	# load the input image from disk
	image = cv2.imread(image_path)

	# load the class labels from disk
	rows = open(labels).read().strip().split("\n")
	classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

	# our CNN requires fixed spatial dimensions for our input image(s)
	# so we need to ensure it is resized to 224x224 pixels while
	# performing mean subtraction (104, 117, 123) to normalize the input;
	# after executing this command our "blob" now has the shape:
	# (1, 3, 224, 224)
	blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

	# load our serialized model from disk
	print("[INFO] loading model...")
	net = cv2.dnn.readNetFromCaffe(prototxt, model)

	# set the blob as input to the network and perform a forward-pass to
	# obtain our output classification
	net.setInput(blob)
	start = time.time()
	preds = net.forward()
	end = time.time()
	print("[INFO] classification took {:.5} seconds".format(end - start))

	# sort the indexes of the probabilities in descending order (higher
	# probabilitiy first) and grab the top-5 predictions
	idxs = np.argsort(preds[0])[::-1][:5]

	# loop over the top-5 predictions and display them
	output_labels =  []
	for (i, idx) in enumerate(idxs):
		# display the predicted label + associated probability to the
		# console	
		output_labels.append(classes[idx])
		print("[INFO] {}. label: {}, probability: {:.5}".format(i + 1,
			classes[idx], preds[0][idx]))

	return output_labels

def character_extractor(image_path):
	image = cv2.imread(image_path)
	text = pytesseract.image_to_string(image)
	return text
	

# image_path = './image.jpg'
# print(label_detection(image_path))
meme_path = '../images/test5.jpg'
print(character_extractor(meme_path))

