from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pandas_implementation import *
from df_text import *
from wordcloud_generator import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		Data_extracted = get_DataFrame(f)
		txt = df_to_text(Data_extracted)
		wc_created = create_wc(txt)

		start_date = Data_extracted['Date'].iloc[0]
		end_date = Data_extracted['Date'].iloc[-1]

		return render_template('index.html', start_date = start_date, end_date = end_date, url ='/static/WordCloud.png')


@app.route('/uploader', methods = ['POST'])
def create_display_wc():
	f = request.files['file']
	Data_extracted = get_DataFrame(f)
	txt = df_to_text(Data_extracted)
	print(txt)
	# wc_created = create_wc(txt)

	return render_template('uploader.html', name = 'new_plot', url ='/static/WordCloud.png')



@app.after_request
def add_header(response):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response


if __name__ == '__main__':
	app.run(debug=True)