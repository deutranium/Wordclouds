import datetime, emoji

def remove_empty_indexes(chats):
	while True:
		try:
			chats.remove("\0")
		except ValueError :
			break
	return chats

def make_list_of_string(input):
	chats = input.read()
	chats = str(chats)
	chats = chats.split("\\n")
	chats[0] = chats[0][2:]   	#removing unwanted initial charecters
	chats[-1] = chats[-1][:-1]  #removing unwanted final charecters

	# Trying to include all messages sent by the same person after
	# the other into a single message
	count_of_NULLS_added = 1
	while(count_of_NULLS_added!=0):
		count_of_NULLS_added = 0
		for i in range(len(chats)):
			if(chats[i] == "\0"):
				continue
			try :
				datetime.datetime.strptime(chats[i].split(",")[0], '%d/%m/%Y')
			except ValueError : 
				try : 
					datetime.datetime.strptime(chats[i].split(",")[0], '%m/%d/%y')
				except ValueError:
					chats[i-1] += " " + chats[i]
					chats[i] = "\0"
					count_of_NULLS_added += 1 

	return remove_empty_indexes(chats)

