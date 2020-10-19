import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)
@app.route('/articles/new', methods=['POST'])
def add_article():
    # Get article from the POST body
    req_data = request.get_json()
    article = req_data['article']
    # Add article to the list
    res_data = helper.add_to_list(article)
    # Return error if article not added
    if res_data is None:
        response = Response("{'error': 'Article not added - " + article + "'}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/articles/all')
def get_articles():
    # Get articles from the helper
    res_data = helper.get_articles()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/articles/delete', methods=['DELETE'])
def delete_article():
    # Get identification from the POST body
    req_data = request.get_json()
    identification = req_data['identification']

    # Delete article from the list
    res_data = helper.delete_article(identification)

    # Return error if the article could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting article - '" + identification +  "}", status=400 , mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response
