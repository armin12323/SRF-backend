from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = 'eb0925df9d8f4ae781ee940422654ead'


@app.route('/fetch_news', methods=['GET'])
def fetch_news():
    topic = request.args.get('query')

    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return jsonify(articles=articles)
    
    
    return jsonify({'msg': 'Error fetching news'}), 500


if __name__ == '__main__':
    app.run(debug=True)
