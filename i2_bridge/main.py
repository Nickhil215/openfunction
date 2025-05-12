 
# Auto-generated Flask Service

from flask import Flask, request, jsonify

import logging

import sys

import os

import typing

import uuid

import re

import requests_toolbelt

import wheel

import astroid

import semver

import abc

import tempfile

import opentelemetry

import app

import requests

import fastapi

import io

import rdflib

import pkg_resources

import i2_bridge

import json

import shutil

import contextlib


app = Flask(__name__)

# Function Definitions

def read():
    """Auto-generated function: read"""
    try:
        response = i2_bridge.setup.read()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def read_requirements(path):
    """Auto-generated function: read_requirements"""
    try:
        response = i2_bridge.setup.read_requirements(path)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def lifespan(context):
    """Auto-generated function: lifespan"""
    try:
        response = i2_bridge.lifespan(context)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_app():
    """Auto-generated function: create_app"""
    try:
        response = i2_bridge.create_app()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_python(github_url, request, branch):
    """Auto-generated function: analyze_python"""
    try:
        response = i2_bridge.analyzer_router.analyze_python(github_url, request, branch)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def setup_telemetry():
    """Auto-generated function: setup_telemetry"""
    try:
        response = i2_bridge.telemetry.setup_telemetry()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def instrument_app(app):
    """Auto-generated function: instrument_app"""
    try:
        response = i2_bridge.telemetry.instrument_app(app)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def semver():
    """Auto-generated function: semver"""
    try:
        response = i2_bridge.config.Settings.semver()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def api_exception_handler(request, exc):
    """Auto-generated function: api_exception_handler"""
    try:
        response = i2_bridge.exceptions.api_exception_handler(request, exc)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_package(package_path, branch):
    """Auto-generated function: analyze_package"""
    try:
        response = i2_bridge.analyzer.analyze_package(package_path, branch)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def upload_to_content_service(content, bearer_token):
    """Auto-generated function: upload_to_content_service"""
    try:
        response = i2_bridge.analyzer.upload_to_content_service(content, bearer_token)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def import_kg(cdn_url, bearer_token):
    """Auto-generated function: import_kg"""
    try:
        response = i2_bridge.analyzer.import_kg(cdn_url, bearer_token)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze(package_path, branch, request):
    """Auto-generated function: analyze"""
    try:
        response = i2_bridge.analyzer.analyze(package_path, branch, request)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_package():
    """Auto-generated function: analyze_package"""
    try:
        response = i2_bridge.source_analyzer.SourceAnalyzer.analyze_package()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def extract_contents():
    """Auto-generated function: extract_contents"""
    try:
        response = i2_bridge.wheel_analyzer.WheelAnalyzer.extract_contents()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_report():
    """Auto-generated function: generate_report"""
    try:
        response = i2_bridge.wheel_analyzer.WheelAnalyzer.generate_report()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def extract_repo_name(github_url):
    """Auto-generated function: extract_repo_name"""
    try:
        response = i2_bridge.base_analyzer.extract_repo_name(github_url)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_pypi_name(repo_name):
    """Auto-generated function: get_pypi_name"""
    try:
        response = i2_bridge.base_analyzer.get_pypi_name(repo_name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def format_path(path):
    """Auto-generated function: format_path"""
    try:
        response = i2_bridge.base_analyzer.format_path(path)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def cleanup():
    """Auto-generated function: cleanup"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.cleanup()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_package():
    """Auto-generated function: analyze_package"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.analyze_package()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def classify_dependencies(packages):
    """Auto-generated function: classify_dependencies"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.classify_dependencies(packages)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_function_imports(node, file_path, source):
    """Auto-generated function: get_function_imports"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.get_function_imports(node, file_path, source)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def infer_package_dependencies(imports):
    """Auto-generated function: infer_package_dependencies"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.infer_package_dependencies(imports)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_used_imports(start_line, end_line, source_code, file_path):
    """Auto-generated function: get_used_imports"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.get_used_imports(start_line, end_line, source_code, file_path)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_package_metrics():
    """Auto-generated function: get_package_metrics"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.get_package_metrics()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def convert_analyzer_to_knowledge_graph():
    """Auto-generated function: convert_analyzer_to_knowledge_graph"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.convert_analyzer_to_knowledge_graph()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_report():
    """Auto-generated function: generate_report"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.generate_report()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_functions_list():
    """Auto-generated function: get_functions_list"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.get_functions_list()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_library_name(package_name):
    """Auto-generated function: get_library_name"""
    try:
        response = i2_bridge.base_analyzer.BaseAnalyzer.get_library_name(package_name)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def parse_requirements(file_path, requirement_info):
    """Auto-generated function: parse_requirements"""
    try:
        response = i2_bridge.git_repository_analyzer.parse_requirements(file_path, requirement_info)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_temp_dir():
    """Auto-generated function: create_temp_dir"""
    try:
        response = i2_bridge.git_repository_analyzer.GitRepositoryAnalyzer.create_temp_dir()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def cleanup():
    """Auto-generated function: cleanup"""
    try:
        response = i2_bridge.git_repository_analyzer.GitRepositoryAnalyzer.cleanup()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_package():
    """Auto-generated function: analyze_package"""
    try:
        response = i2_bridge.git_repository_analyzer.GitRepositoryAnalyzer.analyze_package()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_temp_dir():
    """Auto-generated function: create_temp_dir"""
    try:
        response = i2_bridge.temp_directory_analyzer.TemporaryDirectoryAnalyzer.create_temp_dir()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def extract_contents():
    """Auto-generated function: extract_contents"""
    try:
        response = i2_bridge.temp_directory_analyzer.TemporaryDirectoryAnalyzer.extract_contents()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def analyze_package():
    """Auto-generated function: analyze_package"""
    try:
        response = i2_bridge.temp_directory_analyzer.TemporaryDirectoryAnalyzer.analyze_package()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_extracted_contents():
    """Auto-generated function: process_extracted_contents"""
    try:
        response = i2_bridge.temp_directory_analyzer.TemporaryDirectoryAnalyzer.process_extracted_contents()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_functions(functions):
    """Auto-generated function: add_functions"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.add_functions(functions)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_apis(apis):
    """Auto-generated function: add_apis"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.add_apis(apis)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_tests(tests):
    """Auto-generated function: add_tests"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.add_tests(tests)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_classes(classes):
    """Auto-generated function: add_classes"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.add_classes(classes)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def add_modules(components):
    """Auto-generated function: add_modules"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.add_modules(components)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def export_rdf():
    """Auto-generated function: export_rdf"""
    try:
        response = i2_bridge.rdf_exporter.RDFExporter.export_rdf()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_analyzer(package_path, branch):
    """Auto-generated function: create_analyzer"""
    try:
        response = i2_bridge.package_analyzer_factory.PackageAnalyzerFactory.create_analyzer(package_path, branch)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def extract_contents():
    """Auto-generated function: extract_contents"""
    try:
        response = i2_bridge.compressed_source_analyzer.CompressedSourceAnalyzer.extract_contents()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_report():
    """Auto-generated function: generate_report"""
    try:
        response = i2_bridge.compressed_source_analyzer.CompressedSourceAnalyzer.generate_report()
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API Endpoints

@app.route('/read', methods=['POST'])
def call_read():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return read()

@app.route('/read_requirements', methods=['POST'])
def call_read_requirements():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    path = request_json.get("path")
    

    return read_requirements(path)

@app.route('/lifespan', methods=['POST'])
def call_lifespan():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    context = request_json.get("context")
    

    return lifespan(context)

@app.route('/create_app', methods=['POST'])
def call_create_app():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return create_app()

@app.route('/analyze_python', methods=['POST'])
def call_analyze_python():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    github_url = request_json.get("github_url")
    
    request = request_json.get("request")
    
    branch = request_json.get("branch")
    

    return analyze_python(github_url, request, branch)

@app.route('/setup_telemetry', methods=['POST'])
def call_setup_telemetry():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return setup_telemetry()

@app.route('/instrument_app', methods=['POST'])
def call_instrument_app():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    app = request_json.get("app")
    

    return instrument_app(app)

@app.route('/semver', methods=['POST'])
def call_semver():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return semver()

@app.route('/api_exception_handler', methods=['POST'])
def call_api_exception_handler():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    request = request_json.get("request")
    
    exc = request_json.get("exc")
    

    return api_exception_handler(request, exc)

@app.route('/analyze_package', methods=['POST'])
def call_analyze_package():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    package_path = request_json.get("package_path")
    
    branch = request_json.get("branch")
    

    return analyze_package(package_path, branch)

@app.route('/upload_to_content_service', methods=['POST'])
def call_upload_to_content_service():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    content = request_json.get("content")
    
    bearer_token = request_json.get("bearer_token")
    

    return upload_to_content_service(content, bearer_token)

@app.route('/import_kg', methods=['POST'])
def call_import_kg():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    cdn_url = request_json.get("cdn_url")
    
    bearer_token = request_json.get("bearer_token")
    

    return import_kg(cdn_url, bearer_token)

@app.route('/analyze', methods=['POST'])
def call_analyze():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    package_path = request_json.get("package_path")
    
    branch = request_json.get("branch")
    
    request = request_json.get("request")
    

    return analyze(package_path, branch, request)

@app.route('/analyze_package', methods=['POST'])
def call_analyze_package():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return analyze_package()

@app.route('/extract_contents', methods=['POST'])
def call_extract_contents():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return extract_contents()

@app.route('/generate_report', methods=['POST'])
def call_generate_report():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return generate_report()

@app.route('/extract_repo_name', methods=['POST'])
def call_extract_repo_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    github_url = request_json.get("github_url")
    

    return extract_repo_name(github_url)

@app.route('/get_pypi_name', methods=['POST'])
def call_get_pypi_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    repo_name = request_json.get("repo_name")
    

    return get_pypi_name(repo_name)

@app.route('/format_path', methods=['POST'])
def call_format_path():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    path = request_json.get("path")
    

    return format_path(path)

@app.route('/cleanup', methods=['POST'])
def call_cleanup():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return cleanup()

@app.route('/analyze_package', methods=['POST'])
def call_analyze_package():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return analyze_package()

@app.route('/classify_dependencies', methods=['POST'])
def call_classify_dependencies():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    packages = request_json.get("packages")
    

    return classify_dependencies(packages)

@app.route('/get_function_imports', methods=['POST'])
def call_get_function_imports():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    node = request_json.get("node")
    
    file_path = request_json.get("file_path")
    
    source = request_json.get("source")
    

    return get_function_imports(node, file_path, source)

@app.route('/infer_package_dependencies', methods=['POST'])
def call_infer_package_dependencies():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    imports = request_json.get("imports")
    

    return infer_package_dependencies(imports)

@app.route('/get_used_imports', methods=['POST'])
def call_get_used_imports():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    start_line = request_json.get("start_line")
    
    end_line = request_json.get("end_line")
    
    source_code = request_json.get("source_code")
    
    file_path = request_json.get("file_path")
    

    return get_used_imports(start_line, end_line, source_code, file_path)

@app.route('/get_package_metrics', methods=['POST'])
def call_get_package_metrics():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return get_package_metrics()

@app.route('/convert_analyzer_to_knowledge_graph', methods=['POST'])
def call_convert_analyzer_to_knowledge_graph():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return convert_analyzer_to_knowledge_graph()

@app.route('/generate_report', methods=['POST'])
def call_generate_report():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return generate_report()

@app.route('/get_functions_list', methods=['POST'])
def call_get_functions_list():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return get_functions_list()

@app.route('/get_library_name', methods=['POST'])
def call_get_library_name():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    package_name = request_json.get("package_name")
    

    return get_library_name(package_name)

@app.route('/parse_requirements', methods=['POST'])
def call_parse_requirements():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    file_path = request_json.get("file_path")
    
    requirement_info = request_json.get("requirement_info")
    

    return parse_requirements(file_path, requirement_info)

@app.route('/create_temp_dir', methods=['POST'])
def call_create_temp_dir():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return create_temp_dir()

@app.route('/cleanup', methods=['POST'])
def call_cleanup():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return cleanup()

@app.route('/analyze_package', methods=['POST'])
def call_analyze_package():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return analyze_package()

@app.route('/create_temp_dir', methods=['POST'])
def call_create_temp_dir():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return create_temp_dir()

@app.route('/extract_contents', methods=['POST'])
def call_extract_contents():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return extract_contents()

@app.route('/analyze_package', methods=['POST'])
def call_analyze_package():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return analyze_package()

@app.route('/process_extracted_contents', methods=['POST'])
def call_process_extracted_contents():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return process_extracted_contents()

@app.route('/add_functions', methods=['POST'])
def call_add_functions():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    functions = request_json.get("functions")
    

    return add_functions(functions)

@app.route('/add_apis', methods=['POST'])
def call_add_apis():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    apis = request_json.get("apis")
    

    return add_apis(apis)

@app.route('/add_tests', methods=['POST'])
def call_add_tests():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    tests = request_json.get("tests")
    

    return add_tests(tests)

@app.route('/add_classes', methods=['POST'])
def call_add_classes():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    classes = request_json.get("classes")
    

    return add_classes(classes)

@app.route('/add_modules', methods=['POST'])
def call_add_modules():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    components = request_json.get("components")
    

    return add_modules(components)

@app.route('/export_rdf', methods=['POST'])
def call_export_rdf():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return export_rdf()

@app.route('/create_analyzer', methods=['POST'])
def call_create_analyzer():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    
    package_path = request_json.get("package_path")
    
    branch = request_json.get("branch")
    

    return create_analyzer(package_path, branch)

@app.route('/extract_contents', methods=['POST'])
def call_extract_contents():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return extract_contents()

@app.route('/generate_report', methods=['POST'])
def call_generate_report():
    request_json = request.get_json(silent=True)

    # Extract parameters from request body
    

    return generate_report()


if __name__ == "__main__":
    app.run(port=8080)