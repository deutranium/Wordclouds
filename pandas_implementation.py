import pandas as pd

def clean_data(dirty_Data):
	return dirty_Data[ dirty_Data['Message'] != 'Missing Text' ]

def get_DataFrame(chats):
	# Format ofthe messages is 
	# date, time - Name: Message
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



