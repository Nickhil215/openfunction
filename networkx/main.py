 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import networkx as nx

import warnings

import networkx

import network

import cop


app = Flask(__name__)

# Function Definitions

def add_edge(G, edge_element, edge_attr):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.gexf.GEXFReader.add_edge(G, edge_element, edge_attr)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edge(G, edge_element, graphml_keys):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.graphml.GraphMLReader.add_edge(G, edge_element, graphml_keys)
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

def add_edge(i, p, q):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.flow.networksimplex._DataEssentialsAndFunctions.add_edge(i, p, q)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edge(u_of_edge, v_of_edge):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.digraph.DiGraph.add_edge(u_of_edge, v_of_edge)
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

def to_undirected(reciprocal, as_view):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.digraph.DiGraph.to_undirected(reciprocal, as_view)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_undirected(graph):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.function.to_undirected(graph)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edge(u_for_edge, v_for_edge, key):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.multidigraph.MultiDiGraph.add_edge(u_for_edge, v_for_edge, key)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_undirected(reciprocal, as_view):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.multidigraph.MultiDiGraph.to_undirected(reciprocal, as_view)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_node(node_for_adding):
    """Auto-generated function: add_node"""
    try:
        response = networkx.graph.Graph.add_node(node_for_adding)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edge(u_of_edge, v_of_edge):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.graph.Graph.add_edge(u_of_edge, v_of_edge)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edges_from(ebunch_to_add):
    """Auto-generated function: add_edges_from"""
    try:
        response = networkx.graph.Graph.add_edges_from(ebunch_to_add)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_undirected(as_view):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.graph.Graph.to_undirected(as_view)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edge(u_for_edge, v_for_edge, key):
    """Auto-generated function: add_edge"""
    try:
        response = networkx.multigraph.MultiGraph.add_edge(u_for_edge, v_for_edge, key)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_edges_from(ebunch_to_add):
    """Auto-generated function: add_edges_from"""
    try:
        response = networkx.multigraph.MultiGraph.add_edges_from(ebunch_to_add)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def to_undirected(as_view):
    """Auto-generated function: to_undirected"""
    try:
        response = networkx.multigraph.MultiGraph.to_undirected(as_view)
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

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    G = request_json.get("G")
    
    edge_element = request_json.get("edge_element")
    
    graphml_keys = request_json.get("graphml_keys")
    

    return add_edge(G, edge_element, graphml_keys)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    reciprocal = request_json.get("reciprocal")
    
    as_view = request_json.get("as_view")
    

    return to_undirected(reciprocal, as_view)

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    i = request_json.get("i")
    
    p = request_json.get("p")
    
    q = request_json.get("q")
    

    return add_edge(i, p, q)

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    u_of_edge = request_json.get("u_of_edge")
    
    v_of_edge = request_json.get("v_of_edge")
    

    return add_edge(u_of_edge, v_of_edge)

@app.route('/add_edges_from', methods=['POST'])
def call_add_edges_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    ebunch_to_add = request_json.get("ebunch_to_add")
    

    return add_edges_from(ebunch_to_add)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    reciprocal = request_json.get("reciprocal")
    
    as_view = request_json.get("as_view")
    

    return to_undirected(reciprocal, as_view)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    graph = request_json.get("graph")
    

    return to_undirected(graph)

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    u_for_edge = request_json.get("u_for_edge")
    
    v_for_edge = request_json.get("v_for_edge")
    
    key = request_json.get("key")
    

    return add_edge(u_for_edge, v_for_edge, key)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    reciprocal = request_json.get("reciprocal")
    
    as_view = request_json.get("as_view")
    

    return to_undirected(reciprocal, as_view)

@app.route('/add_node', methods=['POST'])
def call_add_node():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    node_for_adding = request_json.get("node_for_adding")
    

    return add_node(node_for_adding)

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    u_of_edge = request_json.get("u_of_edge")
    
    v_of_edge = request_json.get("v_of_edge")
    

    return add_edge(u_of_edge, v_of_edge)

@app.route('/add_edges_from', methods=['POST'])
def call_add_edges_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    ebunch_to_add = request_json.get("ebunch_to_add")
    

    return add_edges_from(ebunch_to_add)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    as_view = request_json.get("as_view")
    

    return to_undirected(as_view)

@app.route('/add_edge', methods=['POST'])
def call_add_edge():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    u_for_edge = request_json.get("u_for_edge")
    
    v_for_edge = request_json.get("v_for_edge")
    
    key = request_json.get("key")
    

    return add_edge(u_for_edge, v_for_edge, key)

@app.route('/add_edges_from', methods=['POST'])
def call_add_edges_from():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    ebunch_to_add = request_json.get("ebunch_to_add")
    

    return add_edges_from(ebunch_to_add)

@app.route('/to_undirected', methods=['POST'])
def call_to_undirected():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    as_view = request_json.get("as_view")
    

    return to_undirected(as_view)


if __name__ == "__main__":
    app.run(port=8080)