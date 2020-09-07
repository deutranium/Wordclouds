import pandas as pd
import regex as re
import emoji
import datetime

def deEmojify(txt):
	converted=""
	for each in txt:
		if each not in emoji.UNICODE_EMOJI:
			converted = converted + each.lower()
	return converted

def remove_unwanted_texts(txt):
	"""
		Removed messeges are of the type:
			'<media omitted>': Used by whatsapp to tell where a file was uploaded
			"(file attached)": Also Used by whatsapp to tell where a file was uploaded
			"this message was deleted": Used by whatsapp to tell where other users deleted a message
			"you message was deleted":  Used by whatsapp to tell where user deleted a message
		"""
	if (txt != '<media omitted>') & (txt.find("(file attached)")==-1) & (txt !="this message was deleted") & (txt!="you deleted this message"):
		return 1
	else:
		return 0

def correct_dateformat(data):
	for i in range(len(data.Date.iloc[:])):
		if (len(data.Date.iloc[i])==10):
			data.Date.iloc[i] = pd.to_datetime(data.Date.iloc[i], format="%d/%m/%Y")
		else:
			data.Date.iloc[i] = pd.to_datetime(data.Date.iloc[i], format="%m/%d/%y")
	return data

# remove new line characters within individual messages
def convert_chat_arr(chat):
	chat = chat.split('\n')
	l = len(chat)
	# Split by dates
	for i in range(len(chat)):
		try:
			cur_date = chat[i].split(',')[0]

			try:
				datetime.datetime.strptime(cur_date, '%m/%d/%y')
			except:
				datetime.datetime.strptime(cur_date, '%d/%m/%Y')
		except ValueError:
			chat[i-1] = chat[i-1] + ' ' + chat[i]
			chat[i] = "NA"

	# Append "NA" to all the messages which do not start with a date
	for i in range(len(chat)):
		if chat[i].split(' ')[0] == 'NA':
			chat[i] = 'NA'
	while True:
		try:
			chat.remove("NA")
		except ValueError:
			break

	final = []

	for i in chat:
		try:
			matches = re.split('^(.*?)(, | - |: )(.*?)(?!\2)(, | - |: )(.*?)(?!\2|\4)(, | - |: )(.*)', i, re.MULTILINE)
			if remove_unwanted_texts(deEmojify(matches[7])):
				chat_arr = []
				chat_arr.append(matches[1]) # date
				chat_arr.append(matches[3]) # time
				chat_arr.append(matches[5]) # sender
				chat_arr.append(deEmojify(matches[7])) # message
				final.append(chat_arr)
		except:
			continue

	return final


def get_DataFrame(input):
	chat_arr = convert_chat_arr(input)
	chats = pd.DataFrame(chat_arr, columns=["Date", "Time", "Sender", "Message"])
	return correct_dateformat(chats)
