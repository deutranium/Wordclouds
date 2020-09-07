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
	cloud.to_file("./static/WordCloud.png")
	return 1