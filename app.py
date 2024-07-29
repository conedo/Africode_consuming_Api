from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def get_post():
    posts = requests.get(f"{BASE_URL}/posts").json()
    return render_template('posts.html', posts=posts)

@app.route('/comments', methods=['GET'])
def get_comment():
    comments = requests.get(f"{BASE_URL}/comments").json()
    return render_template('comments.html', comments=comments)

@app.route('/albums', methods=['GET'])
def get_albums():
    albums = requests.get(f"{BASE_URL}/albums").json()
    return render_template('albums.html', albums=albums)

@app.route('/photos', methods=['GET'])
def get_photos():
    photos = requests.get(f"{BASE_URL}/photos").json()
    return render_template('photos.html', photos=photos)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = requests.get(f"{BASE_URL}/todos").json()
    return render_template('todos.html', todos=todos)

@app.route('/users', methods=['GET'])
def get_users():
    users = requests.get(f"{BASE_URL}/users").json()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
