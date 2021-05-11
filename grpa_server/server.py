from flask import Flask, request
from flask_socketio import SocketIO

async_mode = "eventlet"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret!'
socket_io = SocketIO(app, async_mode=async_mode)


@socket_io.event
def connect():
    print('Getting connected from ' + request.sid)
    socket_io.emit('start_robot', {"template_name": "Excel.robot"})


@socket_io.event
def disconnect():
    print(request.sid + ' disconnected')


if __name__ == '__main__':
    socket_io.run(app, debug=True)
