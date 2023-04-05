import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file
mode = os.environ.get("MODE")  # get the mode from the environment variables

if mode == "development":
    app = Flask(__name__, template_folder='', static_folder='public', static_url_path='/')    
else:
    app = Flask(__name__, template_folder='dist', static_folder='dist', static_url_path='/')


@app.route('/')
def index():
    return render_template('templates/index.html', title='Rendered from Flask!')


if __name__ == '__main__':
    app.run(debug=True)
