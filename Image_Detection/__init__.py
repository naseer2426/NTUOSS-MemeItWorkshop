# import the necessary packages
import numpy as np
import argparse
import time
import cv2
import pytesseract


def label_detection(image_path):
	#contains a list of all the labels
	labels = './Image_Detection/model/synset_words.txt'

	#config file that defines the model characteristics
	prototxt = './Image_Detection/model/bvlc_googlenet.prototxt'

	#contains the actual weights of each layer of the model
	model = './Image_Detection/model/bvlc_googlenet.caffemodel'

	# load the input image from disk
	image = cv2.imread(image_path)

	# load the class labels from disk
	rows = open(labels).read().strip().split("\n")
	classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

	# our CNN requires fixed spatial dimensions for our input image(s)
	# so we need to ensure it is resized to 224x224 pixels while
	# performing mean subtraction (104, 117, 123) to normalize the input.. we get these values from Image Net training set
	# after executing this command our "blob" now has the shape:
	# (1, 3, 224, 224)
	blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

	# load our serialized model from disk
	net = cv2.dnn.readNetFromCaffe(prototxt, model)

	# set the blob as input to the network and perform a forward-pass to
	# obtain our output classification
	net.setInput(blob)
	preds = net.forward()

	# sort the indexes of the probabilities in descending order (higher
	# probabilitiy first) and grab the top-5 predictions
	idxs = np.argsort(preds[0])[::-1][:5]

	# loop over the top-5 predictions and display them
	output_labels =  []
	for (i, idx) in enumerate(idxs):
		output_labels.append(classes[idx])

	return output_labels

def detect_text(image_path):
    
    #loading image from disk
    image = cv2.imread(image_path)
    
    #using pytesseract to run optical character recognition
    text = pytesseract.image_to_string(image)
    
    text = text.replace('\n', " ")
    
    return text

def final_output(path):
	out = dict()
	out['labels'] = ' , '.join(label_detection(path))
	out['text'] = detect_text(path).replace("\n"," ")
	return out

if __name__=="__main__":
	meme_path = '/Users/abhinav/Desktop/NTUOSS-MemeItWorkshop/Database/Image_Detection/test.jpg'

	print(final_output(meme_path))