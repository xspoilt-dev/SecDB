import requests

SERVER_URL = "http://127.0.0.1:5000/db"


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


if __name__ == "__main__":
    print(create_collection("users"))
    print(insert_document("users", {"name": "Alice", "age": 25}))
    print(insert_many_documents("users", [{"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]))
    print(find_documents("users"))
    print(find_by_field("users", "name", "Alice"))
    print(update_documents("users", {"name": "Alice"}, {"age": 26}))
    print(delete_one_document("users", {"name": "Charlie"}))
    print(delete_many_documents("users", {"age": 30}))
    print(get_all_collections())
    print(get_collection("users"))
    print(drop_collection("users"))
