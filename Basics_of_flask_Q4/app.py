from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_form.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get user input from the form
    user_name = request.form.get('name')
    user_age = request.form.get('age')
    gender = request.form.get('gender')
    email = request.form.get('email')
    message = request.form.get('message')




    # Render the result template with user input
    return render_template('result.html', name=user_name, age=user_age,gender=gender,email=email,message=message)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)