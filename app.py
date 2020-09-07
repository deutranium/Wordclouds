from flask import Flask, render_template, request, g
from PySripts.pandas_implementation import *
from PySripts.df_text import *
from PySripts.wordcloud_generator import *

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
		return render_template('index.html')

@app.route('/', methods = ['POST'])
def temp_code():
	print("posted")
	return 1

if __name__ == '__main__':
		app.run()
