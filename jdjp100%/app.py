from flask import Flask, jsonify, request

app = Flask(__name__)

# przykładowa lista użytkowników
users = [
    {"id": 1, "name": "John", "age": 30},
    {"id": 2, "name": "Hans", "age": 25},
    {"id": 3, "name": "Jean", "age": 40}
]

# Endpoint zwracający 501 Not Implemented dla GET /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'error': 'Not Implemented'}), 501

# Endpoint zwracający przesłany JSON i kod odpowiedzi 201 dla POST /users
@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

# Endpoint zwracający przesłany JSON i kod odpowiedzi 200 dla PUT /users/<id>
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.json
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users[i] = user
            return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

# Endpoint zwracający przesłany JSON i kod odpowiedzi 200 dla PATCH /users/<id>
@app.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    user_data = request.json
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users[i].update(user_data)
            return jsonify(users[i]), 200
    return jsonify({'error': 'User not found'}), 404

# Endpoint zwracający kod odpowiedzi 204 dla DELETE /users/<id>
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            del users[i]
            return '', 204
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
    

jd

