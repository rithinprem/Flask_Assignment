from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins="*")

# Initial tasks
tasks = [
    {'task_id': 1, 'description': 'Buy groceries'},
    {'task_id': 2, 'description': 'Read a book'},
]

@app.route('/')
def index():
    return render_template('todo.html', tasks=tasks)

@socketio.on('update_task')
def handle_update_task(updated_task):
    task_id = updated_task['task_id']

    # Find the task with the given task_id and update its description
    for task in tasks:
        if task['task_id'] == task_id:
            task['description'] = updated_task['description']
            break

    # Broadcast the updated tasks to all connected clients
    emit('updated_tasks', tasks, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=5001,allow_unsafe_werkzeug=True)
