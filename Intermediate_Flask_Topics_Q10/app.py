from flask import Flask, render_template,abort

app = Flask(__name__)

# Custom 404 Error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom 500 Error handler
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# Route for testing 404 error
@app.route('/test_404')
def test_404():
    # Force a 404 error for testing purposes
    abort(404)

# Route for testing 500 error
@app.route('/test_500')
def test_500():
    # Force a 500 error for testing purposes
    1 / 0  # This will raise a ZeroDivisionError

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004)
