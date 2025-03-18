 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import numpy as np

import heterograp

import collection

import dgl

import bas

import collections


app = Flask(__name__)

# Function Definitions

def merge(graphs):
    """Auto-generated function: merge"""
    try:
        response = dgl.merge.merge(graphs)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def hetero_from_shared_memory(name):
    """Auto-generated function: hetero_from_shared_memory"""
    try:
        response = dgl.convert.hetero_from_shared_memory(name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_block(data_dict, num_src_nodes, num_dst_nodes, idtype, device, node_count_check):
    """Auto-generated function: create_block"""
    try:
        response = dgl.convert.create_block(data_dict, num_src_nodes, num_dst_nodes, idtype, device, node_count_check)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def block_to_graph(block):
    """Auto-generated function: block_to_graph"""
    try:
        response = dgl.convert.block_to_graph(block)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_heterogeneous(G, ntypes, etypes, ntype_field, etype_field, metagraph):
    """Auto-generated function: to_heterogeneous"""
    try:
        response = dgl.convert.to_heterogeneous(G, ntypes, etypes, ntype_field, etype_field, metagraph)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_homogeneous(G, ndata, edata, store_type, return_count):
    """Auto-generated function: to_homogeneous"""
    try:
        response = dgl.convert.to_homogeneous(G, ndata, edata, store_type, return_count)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/merge', methods=['POST'])
def call_merge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    graphs = request_json.get("graphs")
    

    return merge(graphs)

@app.route('/hetero_from_shared_memory', methods=['POST'])
def call_hetero_from_shared_memory():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    name = request_json.get("name")
    

    return hetero_from_shared_memory(name)

@app.route('/create_block', methods=['POST'])
def call_create_block():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    data_dict = request_json.get("data_dict")
    
    num_src_nodes = request_json.get("num_src_nodes")
    
    num_dst_nodes = request_json.get("num_dst_nodes")
    
    idtype = request_json.get("idtype")
    
    device = request_json.get("device")
    
    node_count_check = request_json.get("node_count_check")
    

    return create_block(data_dict, num_src_nodes, num_dst_nodes, idtype, device, node_count_check)

@app.route('/block_to_graph', methods=['POST'])
def call_block_to_graph():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    block = request_json.get("block")
    

    return block_to_graph(block)

@app.route('/to_heterogeneous', methods=['POST'])
def call_to_heterogeneous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    G = request_json.get("G")
    
    ntypes = request_json.get("ntypes")
    
    etypes = request_json.get("etypes")
    
    ntype_field = request_json.get("ntype_field")
    
    etype_field = request_json.get("etype_field")
    
    metagraph = request_json.get("metagraph")
    

    return to_heterogeneous(G, ntypes, etypes, ntype_field, etype_field, metagraph)

@app.route('/to_homogeneous', methods=['POST'])
def call_to_homogeneous():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    G = request_json.get("G")
    
    ndata = request_json.get("ndata")
    
    edata = request_json.get("edata")
    
    store_type = request_json.get("store_type")
    
    return_count = request_json.get("return_count")
    

    return to_homogeneous(G, ndata, edata, store_type, return_count)


if __name__ == "__main__":
    app.run(port=8080)