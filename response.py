from flask import Flask, jsonify, request, json
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

@app.route('/twit/<int: twit_id>', methods=['DELETE'])
def delete_twit(twit_id):
    twit = next((t for t in twits if t['id'] == twit_id), None)
    if twit is not None:
        twits.remove(twit)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Twit not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
