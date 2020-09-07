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
	f = request.files['file']
	decoded = f.read().decode('utf-8')
	Data_extracted = get_DataFrame(decoded)
	start_date = request.form.get("start_date")
	end_date = request.form.get("end_date")

	txt = df_to_text(Data_extracted)
	wc_created = create_wc(txt)

	print("posted")
	return render_template('index.html', plot=1, url ='/static/WordCloud.png')

if __name__ == '__main__':
		app.run()
