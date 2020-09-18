from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import os
import main

app = Flask(__name__)
api = Api(app)
port = int(os.environ.get("PORT", 5000))

parser = reqparse.RequestParser()
parser.add_argument('number', type=float, required=True)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

class Prediction(Resource):
    def post(self):
        args = parser.parse_args()
        link = args['link']
        side = args['side']
        res = main.tangram_game(video=link, side=side, prepro=preprocess_img_2, pred_func=get_predictions_with_distances)
        return {'classification report': res}, 200

api.add_resource(HelloWorld, '/hello')
api.add_resource(Prediction, '/prediction')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
