from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    # Get the 'name' parameter from the query string
    name = request.args.get('name', 'Anonymous')
    surname = request.args.get('surname', 'Anonymous')

    # Construct the response JSON
    response_data = {
        'status': 'success',
        'caller_name': name,
        'caller_surname': surname
    }

    # Return the JSON response
    return jsonify(response_data)


@app.route('/get_result', methods=[ 'POST'])
def get_result():
    # Get the 'name' parameter from the query string
    name = request.args.get('name', 'Anonymous')
    surname = request.args.get('surname', 'Anonymous')

    # Construct the response JSON
    response_data = {
        'status': 'success',
        'result': name,
    }
    # go to database and get all trx for name
    # Return the JSON response
    return jsonify(response_data)

if __name__ == '__main__':
    # Run the application on http://127.0.0.1:5000/
    app.run(debug=True)
