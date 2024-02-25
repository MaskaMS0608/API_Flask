from flask import Flask, jsonify, request, json
from json import dumps
from json import JSONEncoder

class Twit:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def to_dict(self):
        return {
            'body': self.body,
            'author': self.author
        }

twits = []
app = Flask(__name__)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder

@app.route('/get_twit', methods=['GET'])
def get_twit():
    twit = Twit("Пример текста", "Автор")
    return twit.to_dict()

@app.route('/twit', methods=['POST'])
def create_twit():
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route('/twit', methods=['GET'])
def read_twit():
    return jsonify({'twits': [twit.to_dict() for twit in twits]})

if __name__ == '__main__':
    app.run(debug=True)
