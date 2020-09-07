from flask import Flask, render_template, request, g
from werkzeug.utils import secure_filename
from PySripts.pandas_implementation import *
from PySripts.df_text import *
from PySripts.wordcloud_generator import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index2.html')

if __name__ == '__main__':
	app.run(debug=True)
