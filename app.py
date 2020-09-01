from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import datetime
import pandas_implementation

app = Flask(__name__)


@app.route('/')
def index():
	# return "Hello World!"
	return render_template('index.html')


# @app.route('/<name>')
# def hello_name(name):
# 	return "Hello {}!".format(name)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		contents = f.read()
		contents = str(contents)
		contents = contents.split("\\n")
		contents[0] = contents[0][2:]
		contents[-1] = contents[-1][:-1]
		for i in range(len(contents)):
			print(i,": ", contents[i])

		print("-"*50)

		count_of_NULLS_added = 1
		while(count_of_NULLS_added!=0):
			count_of_NULLS_added = 0
			for i in range(len(contents)):
				if(contents[i] == "\0"):
					continue
				try :
					datetime.datetime.strptime(contents[i].split(",")[0], '%d/%m/%Y')
				except ValueError:
					contents[i-1] += " " + contents[i]
					contents[i] = "\0"
					count_of_NULLS_added += 1 

		while True:
			try:
				contents.remove("\0")
			except ValueError:
				break

		# for i in range(len(contents)):
		# 	print(i,": ", contents[i])

		contents = pandas_implementation.get_DataFrame(contents)
		print(contents.head())

		return "done"

if __name__ == '__main__':
	app.run(debug=True)
