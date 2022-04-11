import argparse
import json
import os

from flask import Flask as Flask, send_from_directory, request, Response, redirect, url_for
#### only needed for cross-origin requests:
# from flask_cors import CORS
from transformers import pipeline

__author__ = 'Hendrik Strobelt'

app = Flask(__name__)
#### only needed for cross-origin requests:
# CORS(app)

# load sentiment analysis from huggingface
nlp = pipeline('sentiment-analysis')

# redirect requests from root to index.html
@app.route('/')
def hello_world():
    return redirect('client/index.html')

# functional backend taking sentences as request and returning
# sentiment direction and score as JSON result
@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    sentences = request.json['sentences']

    results = [nlp(x) for x in sentences]

    # need to convert from numpy float to regular float for JSON later
    # for res in results[0]:
    #     res["score"]= res["score"].astype(float)

    # return object with request (sentences) and result (sentiments)
    return json.dumps({
        "sentences": sentences,
        "sentiments": results[0]
    })


# just a simple example for GET request
@app.route('/api/data/')
def get_data():
    options = request.args
    name = str(options.get("name", ''))
    y = int(options.get("y", 0))

    res = {
        'name': name,
        'y': [10 * y]
    }
    json_res = json.dumps(res)
    return Response(json_res, mimetype='application/json')

# send everything from client as static content
@app.route('/client/<path:path>')
def send_static(path):
    """ serves all files from ./client/ to ``/client/<path:path>``
    :param path: path from api call
    """
    return send_from_directory('client/', path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodebug", default=False)
    parser.add_argument("--port", default="8888")
    args = parser.parse_args()

    print(args)

    app.run(port=int(args.port), debug=not args.nodebug)
