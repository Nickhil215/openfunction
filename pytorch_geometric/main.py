 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import pytorch_geometric

import os

import os.path as osp


app = Flask(__name__)

# Function Definitions

def get_home_dir():
    """Auto-generated function: get_home_dir"""
    try:
        response = pytorch_geometric.get_home_dir()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/get_home_dir', methods=['POST'])
def call_get_home_dir():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return get_home_dir()


if __name__ == "__main__":
    app.run(port=8080)