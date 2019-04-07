from PIL import Image, ImageDraw, ImageFont
import san_extract
import os
import random
import textwrap
import base64
import cStringIO

font_type = ImageFont.truetype('./static/Ariali.ttf', 18)
	
def create_imgs(disease):
	clean_list = san_extract.get_facts(disease)
	empty_list = []
  	for i in clean_list[:6]:
  		colors = ['yellow', 'palegreen', 'blue', 'orange','pink']
  		image_path = './static/'+ random.choice(colors) +'.jpg' 
		image = Image.open(image_path)
		draw = ImageDraw.Draw(image)
		w,h=650,80
		y_text = h
		#draw.text(xy=(50,150), text=i, fill=(0,0,0), font = font_type)
		i=textwrap.wrap(i,width=40)
		for line in i:
			width,height=font_type.getsize(line)
			draw.text(xy=((w-width)/2, y_text), text=line, fill=(0,0,0), font = font_type, spacing = 0)
			y_text += height
		draw.text(xy=(25, 250), text="#"+disease.replace(" ", "_"), fill=(0,0,0), font = font_type, spacing = 0)
		buffer=cStringIO.StringIO()
		image.save(buffer,format='JPEG')
		img_str=base64.b64encode(buffer.getvalue())
		empty_list.append(img_str)
	return empty_list
		# image.show()
		# print base64.(image)
		# print image.encode(base64)
# img_list=create_imgs("Elon Musk")


