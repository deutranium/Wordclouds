def df_to_text(df):
	chats = df.Message
	chats = [str(chat) for chat in chats]
	text = " ".join(chats)
	return text
