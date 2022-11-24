from crypt import methods
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
import web_final

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def show_index():
    url='https://election.ekantipur.com/?lng=eng'
    web_final.load_update(url)
    return render_template("index1.html",  name = 'new_plot', url ='/static/images/new_plot.png')
if __name__=="__main__":
    app.run(debug=True)