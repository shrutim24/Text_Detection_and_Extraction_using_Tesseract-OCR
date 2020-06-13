import pytesseract
import cv2
import argparse
from pytesseract import Output

'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-c", "--min-conf", type=int, default=0,
	help="mininum confidence value to filter weak text detection")
args = vars(ap.parse_args())
'''

minimum_conf=0
image = cv2.imread("sample_img.png")
rgbvalue = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dict_results = pytesseract.image_to_data(rgbvalue, output_type=Output.DICT)

file = open("output_textfile_conf.txt", "w+") 
file.write("") 
file.close()
for i in range(0, len(dict_results["text"])):
	x = dict_results["left"][i]
	y = dict_results["top"][i]
	w = dict_results["width"][i]
	h = dict_results["height"][i]

	text = dict_results["text"][i]
	conf = int(dict_results["conf"][i])
	if conf > minimum_conf:	
		#print("Confidence: {}".format(conf))
		file = open("output_textfile_conf.txt", "a")
		print("Text: {}".format(text))
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		#text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
		#cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,1.2, (0, 0, 255), 3)
		file.write(text)
		file.write("\n")   
		file.close()
cv2.imshow("Text_OCR", image)
cv2.waitKey(0)