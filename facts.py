import extractor
import wikipedia
import urllib
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def get_image(user_input):
	pg= wikipedia.WikipediaPage(title=user_input)
	html_page = pg.html()
	bs = BeautifulSoup(html_page, 'html.parser')
	use_less="//upload.wikimedia.org/wikipedia/commons/thumb/9/98/Ambox_current_red.svg/42px-Ambox_current_red.svg.png"
	image = bs.findAll('img', height=True)[0]
	if (image.get('src') == use_less):
		image = bs.findAll('img')[1]
	return "https://"+image.get('src')[2:]

def factract(user_input):
	a = extractor.fact_extract(user_input)
	c = a.decode('utf-8') + '\n' 
	c = c.replace("(listen);","")
	return c.encode('utf-8')