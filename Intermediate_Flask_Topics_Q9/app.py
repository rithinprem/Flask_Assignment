from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data 
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author")
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# Route to update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book['title'] = data.get('title', book['title'])
        book['author'] = data.get('author', book['author'])
        return jsonify({"message": "Book updated successfully", "book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003)
