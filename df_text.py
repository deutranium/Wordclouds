def clean_text(in_string):
	in_string = in_string.split(" ")
	while True:
		try:
			in_string.remove("")
		except:
			break
	return " ".join(in_string)

def df_to_text(df):
	chats = df.Message
	chats = [str(chat) for chat in chats]
	text = " ".join(chats)
	return clean_text(text)
