from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

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
		contents = pd.read_csv(secure_filename(f.filename))
		print(contents)
		return "done"

if __name__ == '__main__':
	app.run(debug=True)
