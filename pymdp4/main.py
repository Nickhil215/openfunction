 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import numpy as np

import pymd

import copy

import pymdp


app = Flask(__name__)

# Function Definitions

def update_posterior_policies_full(qs_seq_pi, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma):
    """Auto-generated function: update_posterior_policies_full"""
    try:
        response = pymdp.update_posterior_policies_full(qs_seq_pi, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_posterior_policies_full_factorized(qs_seq_pi, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma):
    """Auto-generated function: update_posterior_policies_full_factorized"""
    try:
        response = pymdp.update_posterior_policies_full_factorized(qs_seq_pi, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_posterior_policies(qs, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma):
    """Auto-generated function: update_posterior_policies"""
    try:
        response = pymdp.update_posterior_policies(qs, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_posterior_policies_factorized(qs, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma):
    """Auto-generated function: update_posterior_policies_factorized"""
    try:
        response = pymdp.update_posterior_policies_factorized(qs, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_expected_states(qs, B, policy):
    """Auto-generated function: get_expected_states"""
    try:
        response = pymdp.get_expected_states(qs, B, policy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_expected_states_interactions(qs, B, B_factor_list, policy):
    """Auto-generated function: get_expected_states_interactions"""
    try:
        response = pymdp.get_expected_states_interactions(qs, B, B_factor_list, policy)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_expected_obs(qs_pi, A):
    """Auto-generated function: get_expected_obs"""
    try:
        response = pymdp.get_expected_obs(qs_pi, A)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_expected_obs_factorized(qs_pi, A, A_factor_list):
    """Auto-generated function: get_expected_obs_factorized"""
    try:
        response = pymdp.get_expected_obs_factorized(qs_pi, A, A_factor_list)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calc_expected_utility(qo_pi, C):
    """Auto-generated function: calc_expected_utility"""
    try:
        response = pymdp.calc_expected_utility(qo_pi, C)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calc_states_info_gain(A, qs_pi):
    """Auto-generated function: calc_states_info_gain"""
    try:
        response = pymdp.calc_states_info_gain(A, qs_pi)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/update_posterior_policies_full', methods=['POST'])
def call_update_posterior_policies_full():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs_seq_pi = request_json.get("qs_seq_pi")
    
    A = request_json.get("A")
    
    B = request_json.get("B")
    
    C = request_json.get("C")
    
    policies = request_json.get("policies")
    
    use_utility = request_json.get("use_utility")
    
    use_states_info_gain = request_json.get("use_states_info_gain")
    
    use_param_info_gain = request_json.get("use_param_info_gain")
    
    prior = request_json.get("prior")
    
    pA = request_json.get("pA")
    
    pB = request_json.get("pB")
    
    F = request_json.get("F")
    
    E = request_json.get("E")
    
    I = request_json.get("I")
    
    gamma = request_json.get("gamma")
    

    return update_posterior_policies_full(qs_seq_pi, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma)

@app.route('/update_posterior_policies_full_factorized', methods=['POST'])
def call_update_posterior_policies_full_factorized():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs_seq_pi = request_json.get("qs_seq_pi")
    
    A = request_json.get("A")
    
    B = request_json.get("B")
    
    C = request_json.get("C")
    
    A_factor_list = request_json.get("A_factor_list")
    
    B_factor_list = request_json.get("B_factor_list")
    
    policies = request_json.get("policies")
    
    use_utility = request_json.get("use_utility")
    
    use_states_info_gain = request_json.get("use_states_info_gain")
    
    use_param_info_gain = request_json.get("use_param_info_gain")
    
    prior = request_json.get("prior")
    
    pA = request_json.get("pA")
    
    pB = request_json.get("pB")
    
    F = request_json.get("F")
    
    E = request_json.get("E")
    
    I = request_json.get("I")
    
    gamma = request_json.get("gamma")
    

    return update_posterior_policies_full_factorized(qs_seq_pi, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, prior, pA, pB, F, E, I, gamma)

@app.route('/update_posterior_policies', methods=['POST'])
def call_update_posterior_policies():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs = request_json.get("qs")
    
    A = request_json.get("A")
    
    B = request_json.get("B")
    
    C = request_json.get("C")
    
    policies = request_json.get("policies")
    
    use_utility = request_json.get("use_utility")
    
    use_states_info_gain = request_json.get("use_states_info_gain")
    
    use_param_info_gain = request_json.get("use_param_info_gain")
    
    pA = request_json.get("pA")
    
    pB = request_json.get("pB")
    
    E = request_json.get("E")
    
    I = request_json.get("I")
    
    gamma = request_json.get("gamma")
    

    return update_posterior_policies(qs, A, B, C, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma)

@app.route('/update_posterior_policies_factorized', methods=['POST'])
def call_update_posterior_policies_factorized():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs = request_json.get("qs")
    
    A = request_json.get("A")
    
    B = request_json.get("B")
    
    C = request_json.get("C")
    
    A_factor_list = request_json.get("A_factor_list")
    
    B_factor_list = request_json.get("B_factor_list")
    
    policies = request_json.get("policies")
    
    use_utility = request_json.get("use_utility")
    
    use_states_info_gain = request_json.get("use_states_info_gain")
    
    use_param_info_gain = request_json.get("use_param_info_gain")
    
    pA = request_json.get("pA")
    
    pB = request_json.get("pB")
    
    E = request_json.get("E")
    
    I = request_json.get("I")
    
    gamma = request_json.get("gamma")
    

    return update_posterior_policies_factorized(qs, A, B, C, A_factor_list, B_factor_list, policies, use_utility, use_states_info_gain, use_param_info_gain, pA, pB, E, I, gamma)

@app.route('/get_expected_states', methods=['POST'])
def call_get_expected_states():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs = request_json.get("qs")
    
    B = request_json.get("B")
    
    policy = request_json.get("policy")
    

    return get_expected_states(qs, B, policy)

@app.route('/get_expected_states_interactions', methods=['POST'])
def call_get_expected_states_interactions():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs = request_json.get("qs")
    
    B = request_json.get("B")
    
    B_factor_list = request_json.get("B_factor_list")
    
    policy = request_json.get("policy")
    

    return get_expected_states_interactions(qs, B, B_factor_list, policy)

@app.route('/get_expected_obs', methods=['POST'])
def call_get_expected_obs():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs_pi = request_json.get("qs_pi")
    
    A = request_json.get("A")
    

    return get_expected_obs(qs_pi, A)

@app.route('/get_expected_obs_factorized', methods=['POST'])
def call_get_expected_obs_factorized():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qs_pi = request_json.get("qs_pi")
    
    A = request_json.get("A")
    
    A_factor_list = request_json.get("A_factor_list")
    

    return get_expected_obs_factorized(qs_pi, A, A_factor_list)

@app.route('/calc_expected_utility', methods=['POST'])
def call_calc_expected_utility():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    qo_pi = request_json.get("qo_pi")
    
    C = request_json.get("C")
    

    return calc_expected_utility(qo_pi, C)

@app.route('/calc_states_info_gain', methods=['POST'])
def call_calc_states_info_gain():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    A = request_json.get("A")
    
    qs_pi = request_json.get("qs_pi")
    

    return calc_states_info_gain(A, qs_pi)


if __name__ == "__main__":
    app.run(port=8080)