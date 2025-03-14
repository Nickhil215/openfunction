 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import import dgl.sparse as dglsp

import from dgl.data import dgl.data.CoraGraphDataset


app = Flask(__name__)

# Function Definitions

def hypergraph_laplacian(H):
    """Auto-generated function: hypergraph_laplacian"""
    try:
        response = dgl...sparse.hypergraphatt.hypergraph_laplacian(H)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/hypergraph_laplacian', methods=['POST'])
def call_hypergraph_laplacian():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    H = request_json.get("H")
    

    return hypergraph_laplacian(H)


if __name__ == "__main__":
    app.run(port=8080)