from flask import Flask, request, jsonify
from secdb import SecDB

app = Flask(__name__)
db = SecDB()

@app.route("/db/<action>", methods=["POST"])
def handle_request(action):
    data = request.json
    if action == "create_collection":
        return jsonify(db.create_collection(data.get("collection_name")))
    elif action == "drop_collection":
        return jsonify({"success": True, "message": db.drop_collection(data.get("collection_name"))})
    elif action == "insert":
        return jsonify(db.insert(data.get("collection_name"), data.get("document")))
    elif action == "insert_many":
        return jsonify(db.insert_many(data.get("collection_name"), data.get("documents")))
    elif action == "find":
        return jsonify(db.find(data.get("collection_name"), data.get("query")))
    elif action == "find_by_field":
        return jsonify(db.find_by_field(data.get("collection_name"), data.get("field"), data.get("value")))
    elif action == "get_all_collections":
        return jsonify({"success": True, "collections": db.get_all_collections()})
    elif action == "get_all_documents":
        return jsonify({"success": True, "data": db.get_all_documents()})
    elif action == "get_collection":
        collection_name = data.get("collection_name")
        return jsonify({"success": True, "collection": db.get_collection(collection_name)})
    elif action == "update":
        return jsonify(db.update(data.get("collection_name"), data.get("query"), data.get("updates")))
    elif action == "delete_one":
        return jsonify(db.delete_one(data.get("collection_name"), data.get("query")))
    elif action == "delete_many":
        return jsonify(db.delete_many(data.get("collection_name"), data.get("query")))
    return jsonify({"success": False, "message": "Invalid action."})

if __name__ == "__main__":
    app.run(debug=True)
