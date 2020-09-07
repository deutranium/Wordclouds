from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

def create_wc(text):
	cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS)).generate(text)
	cloud.to_file("./static/WordCloud.png")
	return 1