from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_dynamic.html')

@app.route('/greet')
def greet():
    # Get the 'name' parameter from the URL
    user_name = request.args.get('name')
    return render_template('greet.html', name=user_name)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)
