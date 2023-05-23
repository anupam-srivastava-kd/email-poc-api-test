from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route to handle the POST request
@app.route('/api/data', methods=['POST'])
def post_data():
    # Extract the data from the request body
    data = request.get_json()

    # Process the data or perform any desired operations
    # For this example, let's just echo the received data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
