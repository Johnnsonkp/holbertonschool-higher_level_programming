from flask import Flask, jsonify, request

app = Flask(__name__)

class UserStore:
  def __init__(self):
    self.user_data = {
      "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, 
      "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

  def get_user_data(self):
    return self.user_data
  
  def get_users(self):
    users = []

    for user_name, info in self.user_data.items():
        users.append(user_name)
    return users
  
  def add_user(self, new_user_dets):
    self.user_data[new_user_dets['username']] = new_user_dets


user_store = UserStore()

@app.route('/add_user', methods=['POST'])
def add_new_user():

  try:
    new_user_details = request.get_json()

    if 'username' not in new_user_details:
      return jsonify({"error": "Username is required"}), 400
    
    user_store.add_user(new_user_details)
    return jsonify({"message": "User added", "user": new_user_details}), 201

  except Exception as e: 
    return jsonify({"error": str(e)}), 500
  


@app.route('/users/<username>', methods=['GET'])
def show_user_info(username):
  user_data = user_store.get_user_data()
  user = user_data[username]

  try: 
    return jsonify(user)
  except KeyError: 
    return jsonify({"error": "User not found"}), 404



@app.route('/status', methods=['GET'])
def show_app_status():
  return "OK", 200


@app.route('/data', methods=['GET'])
def users():
  return jsonify(user_store.get_users())



@app.route('/', methods=['GET'])
def home():
  return "Welcome to the Flask API!"

if __name__ == '__main__': app.run(debug=True)
