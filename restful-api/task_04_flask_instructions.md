## Flask API Guide

Flask is a lightweight Python web framework, ideal for building small to medium web applications and RESTful APIs.

#### Prerequisites

- Python installed

- Flask installed (pip install Flask)

#### Setup

1. Install Flask:

    `pip install Flask`

2. Create a Python file (e.g., app.py) and import Flask:

``` python 
  from flask import Flask
  app = Flask(__name__)
```

#### Creating Endpoints

###### Basic Route

``` python
@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == "__main__":
    app.run()
```
Run the server and visit http://localhost:5000.

###### Serving JSON Data

```
from flask import jsonify

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
}

@app.route('/data')
def get_users():
    return jsonify(list(users.keys()))
```

###### Additional Endpoints

Status Check

``` python
@app.route('/status')
def status():
    return "OK"
```

User Details

``` python
@app.route('/users/<username>')
def get_user(username):
    return jsonify(users.get(username, {"error": "User not found"}))
```

###### Handling POST Requests

``` python
from flask import request

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201
```

###### Testing

Run the server

``` python
flask --app app.py run
```

Test with curl

``` python
curl -X POST http://localhost:5000/add_user -H "Content-Type: application/json" -d '{"username": "alice", "name": "Alice", "age": 25, "city": "San Francisco"}'
```
``` python
Expected response

{
    "message": "User added",
    "user": {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
}
```

###### Notes

- Use @app.route() to define routes.

- Dynamic routes (e.g., /users/<username>) allow capturing values.

- jsonify() converts Python data to JSON responses.

- Flask reloads on code changes but may require a restart for new files.


