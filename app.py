from crypt import methods
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
import web_final

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/load_api', methods=['POST'])
def load_api():
    data =request.json['data']
    print(data)
    return jsonify(data)

@app.route('/load', methods=['POST'])
def load():
    #data=[float(x) for x in request.form.values()]
    #x=5
    url='https://election.ekantipur.com/?lng=eng'
    web_final.load_update(url)
    return render_template('index.html', name = 'Federal Parliment Update', url ='/static/images/new_plot.png', 
            url1='/static/images/provincial_plot.png', url2 ='samanu_plot.png')

if __name__=="__main__":
    app.run(debug=True)