 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import requests

import requests.sessions


app = Flask(__name__)

# Function Definitions

def hello_world10(url, params):
    """Auto-generated function: hello_world10"""
    try:
        response = requests.api.get(url, params)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def fetch_data1(api_url, headers):
    """Auto-generated function: fetch_data1"""
    try:
        response = requests.get(api_url, headers)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/hello_world10', methods=['POST'])
def call_hello_world10():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    url = request_json.get("url")
    
    params = request_json.get("params")
    

    return hello_world10(url, params)

@app.route('/fetch_data1', methods=['POST'])
def call_fetch_data1():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    api_url = request_json.get("api_url")
    
    headers = request_json.get("headers")
    

    return fetch_data1(api_url, headers)


if __name__ == "__main__":
    app.run(port=8080)