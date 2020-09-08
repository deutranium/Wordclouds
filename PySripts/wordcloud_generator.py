from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from io import BytesIO

stopwords = set(STOPWORDS)

def create_wc(text):
	"""
		Creates and saves a wordcloud image(WordCloud.png) from a non-empty 
		input string.
		"""
	cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS)).generate(text)
	cloud.to_file("./static/WordCloud.png")
	return 1