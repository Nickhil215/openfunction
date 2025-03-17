 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import requests


app = Flask(__name__)

# Function Definitions

def test_function(param1, param2):
    """Auto-generated function: test_function"""
    try:
        response = requests.get('https://api.example.com')
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/test_function', methods=['POST'])
def call_test_function():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    param1 = request_json.get("param1")
    
    param2 = request_json.get("param2")
    

    return test_function(param1, param2)


if __name__ == "__main__":
    app.run(port=8080)