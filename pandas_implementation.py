import pandas as pd
from txt_to_array_of_messages import *

def clean_data(dirty_Data):
	dirty_Data['Date'] = pd.to_datetime(dirty_Data['Date'])
	return dirty_Data[ dirty_Data['Message'] != 'Missing Text' ]


def get_DataFrame(input):

	chats = make_list_of_string(input)
	
	dates = [chat.split(',')[0] for chat in chats]
	times = [chat.split(',')[1].split("-")[0].strip(" ") for chat in chats]
	names = [chat.split('-')[1].split(":")[0] for chat in chats]
	content = []
	for i in range(len(chats)):
		try:
			content.append(chats[i].split(':')[2])
		except IndexError:
			content.append('Missing Text')

	result = pd.DataFrame(list(zip(dates, times, names, content)), columns = ['Date', 'Time', 'Name', 'Message'])

	return clean_data(result)



