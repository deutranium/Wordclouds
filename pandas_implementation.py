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
			chat_arr = []

			# generates ['', 'date', ', ', 'time', ' - ', 'sender', ': ', 'message', '']
			matches = re.split('^(.*?)(, | - |: )(.*?)(?!\2)(, | - |: )(.*?)(?!\2|\4)(, | - |: )(.*)', i, re.MULTILINE)

			chat_arr.append(matches[1])	# date
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

	return chats
