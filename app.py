import os
from flask import Flask, request

app = Flask(__name__)

# Sample data - imagine it comes from a database
users = [
    {"id": 1, "username": "john"},
    {"id": 2, "username": "jane"},
    {"id": 3, "username": "alice"}
]
next_user_id = 4

"""
Getting all users
"""
@app.route('/users', methods=['GET'])
def get_users():
    return ", ".join([user["username"] for user in users])

"""
Getting just the user with the specified id
"""
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user["username"] for user in users if user['id'] == user_id), None)
    if user:
        return user
    else:
        return "Error: User not found", 404

"""
Adding a new user into users
"""
@app.route('/users', methods=['POST'])
def create_user():
    if 'username' not in request.form.keys():
        return "Error: Username is required", 400
    global next_user_id
    user_id = next_user_id
    next_user_id += 1
    username = request.form['username']
    user = {
        'id': user_id,
        'username': username
    }
    users.append(user)
    return f"User {username} created with id {user_id}", 201

"""
Updating the specifid user's id
"""
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return "Error: User not found", 404
    if 'username' not in request.form.keys():
        return "Error: Username is required", 400
    user['username'] = request.form['username']
    return f"Id {user_id} updated with username {user['username']}", 200

"""
Deleting a user
"""
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return "Message: User deleted"

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
