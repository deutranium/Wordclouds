import pandas as pd
from txt_to_array_of_messages import *
import re
import emoji
import datetime

def clean_data(dirty_Data):
	dirty_Data['Date'] = pd.to_datetime(dirty_Data['Date'])
	return dirty_Data[ dirty_Data['Message'] != 'Missing Text' ]


def deEmojify(txt):
	converted=""

	for each in txt:
		if each not in emoji.UNICODE_EMOJI:
			converted = converted + each
	return converted


# remove new line characters within individual messages
def convert_chat_arr(chat):
	chat = chat.splitlines()
	l = len(chats)
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
			chat_arr.append(i.split(', ')[0])
			chat_arr.append(i.split(', ')[1].split(' - ')[0])
			chat_arr.append(i.split(', ')[1].split(' - ')[1].split(':')[0])
			chat_arr.append(deEmojify(i.split(', ')[1].split(' - ')[1].split(':')[1]))
			final.append(chat_arr)
		except:
			continue

	return final


def get_DataFrame(input):

	chat_arr = convert_chat_arr(input)


	# chat_arr contains the 2D array, need to convert it

	content = []
	for i in range(len(chats)):
		try:
			content_i = chats[i].split(':')[2]
			content.append(content_i)
		except IndexError:
			content.append('Missing Text')

	result = pd.DataFrame(list(zip(dates, times, names, content)), columns = ['Date', 'Time', 'Name', 'Message'])

	return clean_data(result)
