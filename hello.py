from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def post(self, path_param):
        json_request = request.get_json()

        print("Path parameter: \"{0}\"".format(path_param))
        print("json_string: \"{0}\"".format(json_request))
        for key in json_request.keys():
            print("\"{0}\": \"{1}\"".format(key, json_request[key]))


api.add_resource(Test, "/<string:path_param>")
