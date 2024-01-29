from flask import Flask, render_template
from flask_socketio import SocketIO,emit

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('notify_update')
def handle_notification(data):
    message = data.get('message', 'Update!')
    emit('update_notification', {'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',allow_unsafe_werkzeug=True)
