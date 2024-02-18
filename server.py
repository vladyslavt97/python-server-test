from flask import Flask, jsonify

app = Flask(__name__)

# Define the route /get/users


@app.route('/get/users', methods=['GET'])
def get_users():
    # Simulate fetching user data (replace with your actual data retrieval logic)
    users = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'},
        {'id': 3, 'name': 'Bob'}
    ]

    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
