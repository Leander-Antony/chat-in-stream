from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import SocketIO, send
import uuid
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
user_sessions = {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if password == 'astridonvacation':
            uid = str(uuid.uuid4())
            session['username'] = username
            session['uid'] = uid
            user_sessions[uid] = username
            return redirect(url_for('chat'))
        else:
            return render_template('login.html', error="Wrong password.")

    return render_template('login.html')

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'], uid=session['uid'])
    return redirect('/')

@socketio.on('message')
def handleMessage(data):
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)