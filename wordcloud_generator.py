import flask
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pandas as pd
from io import BytesIO

stopwords = set(STOPWORDS)

def create_wc(text):
	cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS)).generate(text)
	plt.imshow(cloud, interpolation='bilinear')
	plt.axis("off")
	img = BytesIO()
	plt.savefig(img)
	img.seek(0)
	return flask.send_file(img, mimetype='image/png')

a = create_wc("ab ab ab ab ab ab ab ab cd cd ef ef ef ef ef ab ab ab ab ab ab ef gh ij kl mn op qr st uv wx wx wx yz")
a = a.save("abcdefg")
