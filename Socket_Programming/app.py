from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message, broadcast=True)

@socketio.on('image')
def handle_image(image_data):
    print('received image: ' + image_data)
    emit('image', image_data, broadcast=True)

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)