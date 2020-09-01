from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pandas_implementation import *

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
		Data_extracted = get_DataFrame(f)
		print(Data_extracted.head())		
		return "done"

if __name__ == '__main__':
	app.run(debug=True)
