 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

string


app = Flask(__name__)

# Function Definitions

def string(string):
    """Auto-generated function: string"""
    try:
        response = string
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/string', methods=['POST'])
def call_string():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    string = request_json.get("string")
    

    return string(string)


if __name__ == "__main__":
    app.run(port=8080)