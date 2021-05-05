from flask import Flask, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO
import robot

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


class Test(Resource):
    @socketio.on('json')
    def post(self, path_param, json):
        json_request = request.get_json()
        print('received json: ' + str(json))
        print("Path parameter: \"{0}\"".format(path_param))
        print("json_string: \"{0}\"".format(json_request))
        for key in json_request.keys():
            print("\"{0}\": \"{1}\"".format(key, json_request[key]))
        logFile = open('mylog.txt', 'w')
        robot.run("Excel.robot", stdout=logFile)

api.add_resource(Test, "/<string:path_param>")

if __name__ == "__main__":
    socketio.run(app)
