from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/process', methods=['POST'])
def process_data():
    data = request.json

    print(f'this is data : \n{data}\n')
    
    input_value = data['inputValue']

    print(f'this is input val : {input_value}')

    return_val = something(input_value)

    result = {'message': f"Recieved Input: {return_val}"}
    
    return jsonify(result)


def something(json_item):

    print(f'this is the json item: {json_item}')

    if json_item == 'yosef':
        return 'is gay'

    elif json_item == 'fateh':
        return 'DootyBUTT'
    
    else:
        return 'weirdo'


if __name__ == '__main__':
    app.run(debug=True)
