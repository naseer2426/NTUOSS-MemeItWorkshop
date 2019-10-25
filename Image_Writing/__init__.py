def make_meme(string,filename,isWhite=True, optional=1):
	from PIL import ImageFont,Image,ImageDraw
	from math import ceil
	def char_per_line(imgWidth, padding,fontSize):
		char_num = ceil(((0.9*imgWidth-(2*padding))/fontSize))
		return char_num

	def add_newline_char(caption,line_size):
		temp = caption.split(' ')
		counter = 0
		output = ''
		for i in temp:
			counter+=len(i)
			if(counter>line_size):
				output+=i+'\n'
				counter = 0
			else:
				output+=i+' '
		return output
	string = string.replace('\n',' ')

	img =  Image.open(filename)
	draw = ImageDraw.Draw(img)
	imageSize = img.size
	fontRatio = 0.03
	paddingRatio = 0.05
	fontSize = int(imageSize[1]*fontRatio)
	font = ImageFont.truetype("/Library/Fonts/Impact.ttf", fontSize)
	padding = ceil(paddingRatio*imageSize[0])
	char_num = char_per_line(imageSize[0], padding, fontSize)
	string = add_newline_char(string,char_num)
	pos = tuple(map(lambda x: x*paddingRatio,imageSize))
	if(isWhite):
		colour=(255,255,255,255)
	else:
		colour=(0,0,0,255)
	draw.text(pos,string, font=font, fill=colour)
	img.save("Completed/output"+str(optional)+".png")

if __name__ == "__main__":
	make_meme("/Users/ashivalagar/Desktop/NTUOSS-MemeItWorkshop/Completed/output2.png".replace('/',' ').replace('-',' '),'/Users/ashivalagar/Desktop/NTUOSS-MemeItWorkshop/Completed/output2.png',True ,6)