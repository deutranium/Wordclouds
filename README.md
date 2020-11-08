# Wordcloud Generator

Live: [https://wa-wc.herokuapp.com/](https://wa-wc.herokuapp.com/)

*Works only for chats retrived using WhatsApp installed on an Android device*

## Setup

Please ensure you have the following installed

- Flask>=1.1.1

- Python>=3.8.1

- pip3 >= 9.0.1

Follow the steps below once the above requirements are satisfied

- Clone the repo using `git clone https://github.com/deutranium/wordclouds.git`

- `cd` into the repo and install the required modules using `pip3 install -r requirements.txt`

- You can now run the app with `python3 app.py`

## To repo

- Use `git push origin master` to push your changes

## Staging Area

To test the app on server before pushing it to final phase

- Add staging app to repo using `git remote add stage git@heroku.com:wordcloud-flask-stage.git`. This might get an error if the SSH keys of your machine aren't saved on the server

- To push to staging, use `git push stage master`

## Production Area

To test the app on server before pushing it to final phase

- Add staging app to repo using `git remote add pro git@heroku.com:wa-wc.git`. This might get an error if the SSH keys of your machine aren't saved on the server

- To push to production, use `git push pro master`
