from flask import Flask, render_template, request, g
from werkzeug.utils import secure_filename
from PySripts.pandas_implementation import *
from PySripts.df_text import *
from PySripts.wordcloud_generator import *

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
		return "Hello World!"

if __name__ == '__main__':
		app.run()
