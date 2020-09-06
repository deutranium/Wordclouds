import re

def clean_text(in_string):
	in_string = in_string.split(" ")
	while True:
		try:
			in_string.remove("")
		except:
			break
	return " ".join(in_string)

def deEmojify(text):
	emoji_pattern = re.compile(
	u"(\ud83d[\ude00-\ude4f])|"  # emoticons
	u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
	u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
	u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
	u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
	"+", flags=re.UNICODE)
	return emoji_pattern.sub(r'',text)

def df_to_text(df):
	chats = df.Message
	chats = [str(chat) for chat in chats]
	text = " ".join(chats)
	return clean_text(deEmojify(text))
