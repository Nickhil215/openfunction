 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

from torch_geometric.datasets import torch_geometric.datasets.Planetoid

from torch_geometric.data import torch_geometric.data.Data

from torch import torch.Tensor

import torch_geometric.transforms as T

from torch_geometric.utils import torch_geometric.utils.one_hot

import torch

import torch.nn.functional as F

import os.path as osp

import pytorch_geometric


app = Flask(__name__)

# Function Definitions

def test(U, y_one_hot, data):
    """Auto-generated function: test"""
    try:
        response = pytorch_geometric.examples.ogc.LinearNeuralNetwork.test(U, y_one_hot, data)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/test', methods=['POST'])
def call_test():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    U = request_json.get("U")
    
    y_one_hot = request_json.get("y_one_hot")
    
    data = request_json.get("data")
    

    return test(U, y_one_hot, data)


if __name__ == "__main__":
    app.run(port=8080)