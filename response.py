from flask import Flask, jsonify, request
import json
from model.twit import Twit

twits = []
app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {"body": obj.body, "author": obj.author}
        else:
            return super().default(obj)


app.json_encoder = CustomJSONEncoder


@app.route("/twit", methods=["GET"])
def read_twits():
    return jsonify({"twits": [twit.to_dict() for twit in twits]})


@app.route("/twit", methods=["POST"])
def create_twit():
    """{"body": "Hello", "author": "MS"}"""
    twit_json = request.get_json()
    twit = Twit(twit_json["body"], twit_json["author"])
    twits.append(twit)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
