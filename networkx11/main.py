 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import networkx

import cop

import networkx as nx


app = Flask(__name__)

# Function Definitions

def add_edge(G, edge_element, edge_attr):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.gexf.GEXFReader.add_edge(G, edge_element, edge_attr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_undirected(reciprocal, as_view):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.planarity.PlanarEmbedding.to_undirected(reciprocal, as_view)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edges_from(ebunch_to_add):
    """Auto-generated function: add_edges_from"""
    try:
        response = networkx.digraph.DiGraph.add_edges_from(ebunch_to_add)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    G = request_json.get("G")
    
    edge_element = request_json.get("edge_element")
    
    edge_attr = request_json.get("edge_attr")
    

    return add_edge(G, edge_element, edge_attr)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    reciprocal = request_json.get("reciprocal")
    
    as_view = request_json.get("as_view")
    

    return to_undirected(reciprocal, as_view)

@app.route('/add_edges_from', methods=['POST'])
def call_add_edges_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    ebunch_to_add = request_json.get("ebunch_to_add")
    

    return add_edges_from(ebunch_to_add)


if __name__ == "__main__":
    app.run(port=8080)