import requests

SERVER_URL = "<server_url>/db"


def send_request(action, data):
    response = requests.post(f"{SERVER_URL}/{action}", json=data)
    return response.json()

def create_collection(name):
    return send_request("create_collection", {"collection_name": name})

def drop_collection(name):
    return send_request("drop_collection", {"collection_name": name})


def insert_document(collection_name, document):
    return send_request("insert", {"collection_name": collection_name, "document": document})

def insert_many_documents(collection_name, documents):
    return send_request("insert_many", {"collection_name": collection_name, "documents": documents})


def find_documents(collection_name, query=None):
    return send_request("find", {"collection_name": collection_name, "query": query})

def find_by_field(collection_name, field, value):
    return send_request("find_by_field", {"collection_name": collection_name, "field": field, "value": value})

def get_all_collections():
    return send_request("get_all_collections", {})

def get_all_documents():
    return send_request("get_all_documents", {})

def get_collection(collection_name):
    return send_request("get_collection", {"collection_name": collection_name})


def update_documents(collection_name, query, updates):
    return send_request("update", {"collection_name": collection_name, "query": query, "updates": updates})


def delete_one_document(collection_name, query):
    return send_request("delete_one", {"collection_name": collection_name, "query": query})

def delete_many_documents(collection_name, query):
    return send_request("delete_many", {"collection_name": collection_name, "query": query})
