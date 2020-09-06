import pandas as pd
import re
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
			# chat_arr = re.split(', | - |: ', i)
			# chat_arr[3] = deEmojify(chat_arr[3])

			# print(chat_arr)
			chat_arr = []
			chat_arr.append(i.split(', ')[0])
			chat_arr.append(i.split(', ')[1].split(' - ')[0])
			chat_arr.append(i.split(', ')[1].split(' - ')[1].split(':')[0])
			chat_arr.append(deEmojify("".join(i.split(', ')[1].split(' - ')[1].split(':'))))
			final.append(chat_arr)
		except:
			continue

	return final


def get_DataFrame(input):

	chat_arr = convert_chat_arr(input)
	chats = pd.DataFrame(chat_arr, columns=["Date", "Time", "Sender", "Message"])

	return chats
