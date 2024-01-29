from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'  

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return render_template('index_session.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(host="0.0.0.0")
