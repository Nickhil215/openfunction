 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

from neo4j.testkitbackend.backend import Request

import tomlkit

from neo4j.setup import changed_package_name

from neo4j.docs.source.conf import setup

from neo4j.setup import change_project_name

from contextlib import contextmanager


app = Flask(__name__)

# Function Definitions

def change_project_name(new_name):
    """Auto-generated function: change_project_name"""
    try:
        response = neo4j-python-driver.setup.change_project_name(new_name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def changed_package_name(new_name):
    """Auto-generated function: changed_package_name"""
    try:
        response = neo4j-python-driver.setup.changed_package_name(new_name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get(item, default):
    """Auto-generated function: get"""
    try:
        response = neo4j.testkitbackend.backend.Request.get(item, default)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mark_all_as_read(recursive):
    """Auto-generated function: mark_all_as_read"""
    try:
        response = neo4j.testkitbackend.backend.Request.mark_all_as_read(recursive)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mark_item_as_read(item, recursive):
    """Auto-generated function: mark_item_as_read"""
    try:
        response = neo4j.testkitbackend.backend.Request.mark_item_as_read(item, recursive)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mark_item_as_read_if_equals(item, value, recursive):
    """Auto-generated function: mark_item_as_read_if_equals"""
    try:
        response = neo4j.testkitbackend.backend.Request.mark_item_as_read_if_equals(item, value, recursive)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def unseen_keys():
    """Auto-generated function: unseen_keys"""
    try:
        response = neo4j.testkitbackend.backend.Request.unseen_keys()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def seen_all_keys():
    """Auto-generated function: seen_all_keys"""
    try:
        response = neo4j.testkitbackend.backend.Request.seen_all_keys()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def setup(app):
    """Auto-generated function: setup"""
    try:
        response = neo4j.docs.source.conf.setup(app)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/change_project_name', methods=['POST'])
def call_change_project_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    new_name = request_json.get("new_name")
    

    return change_project_name(new_name)

@app.route('/changed_package_name', methods=['POST'])
def call_changed_package_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    new_name = request_json.get("new_name")
    

    return changed_package_name(new_name)

@app.route('/get', methods=['POST'])
def call_get():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    item = request_json.get("item")
    
    default = request_json.get("default")
    

    return get(item, default)

@app.route('/mark_all_as_read', methods=['POST'])
def call_mark_all_as_read():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    recursive = request_json.get("recursive")
    

    return mark_all_as_read(recursive)

@app.route('/mark_item_as_read', methods=['POST'])
def call_mark_item_as_read():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    item = request_json.get("item")
    
    recursive = request_json.get("recursive")
    

    return mark_item_as_read(item, recursive)

@app.route('/mark_item_as_read_if_equals', methods=['POST'])
def call_mark_item_as_read_if_equals():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    item = request_json.get("item")
    
    value = request_json.get("value")
    
    recursive = request_json.get("recursive")
    

    return mark_item_as_read_if_equals(item, value, recursive)

@app.route('/unseen_keys', methods=['POST'])
def call_unseen_keys():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return unseen_keys()

@app.route('/seen_all_keys', methods=['POST'])
def call_seen_all_keys():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return seen_all_keys()

@app.route('/setup', methods=['POST'])
def call_setup():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    app = request_json.get("app")
    

    return setup(app)


if __name__ == "__main__":
    app.run(port=8080)