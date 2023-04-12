from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Hans", "age": 25},
    {"id": 3, "name": "Jean", "age": 40}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'error': 'Not Implemented'}), 501

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.json
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users[i] = user
            return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    user_data = request.json
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users[i].update(user_data)
            return jsonify(users[i]), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            del users[i]
            return '', 204
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
    


