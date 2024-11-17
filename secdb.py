__author__ = "Minhajul Islam"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Minhajul Islam"
__email__ = "x_spoilt@yahoo.com"
__status__ = "Testing"
__tool__ = "SecDB"

"""
A simple, secure, and lightweight database for Python applications.

Encryption : AES-256-CBC
Key Derivation : SHA-256

Database Type : NoSQL (Document-based)

"""
import json
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64

class SecDB:
    def __init__(self, db_name='xdatabase', password='pwd@123', file_path=None):
        self.db_name = db_name
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = f"{db_name}.secdb"
        self.password = password
        self.key = self._generate_key(password)
        self.block_size = 16
        if os.path.exists(self.file_path):
            self.data = self._load_encrypted_data()
        else:
            self.data = {}

    def _generate_key(self, password):
        """Generate a 32-byte key using the provided password."""
        return hashlib.sha256(password.encode()).digest()

    def _encrypt_data(self, data):
        """Encrypt data using AES encryption."""
        cipher = AES.new(self.key, AES.MODE_CBC)
        json_data = json.dumps(data).encode()
        padded_data = pad(json_data, self.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return base64.b64encode(cipher.iv + encrypted_data).decode()

    def _decrypt_data(self, encrypted_data):
        """Decrypt data using AES encryption."""
        encrypted_data = base64.b64decode(encrypted_data)
        iv = encrypted_data[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data[self.block_size:]), self.block_size)
        return json.loads(decrypted_data.decode())

    def _load_encrypted_data(self):
        """Load data from the encrypted file."""
        try:
            with open(self.file_path, 'r') as file:
                encrypted_data = file.read()
                return self._decrypt_data(encrypted_data)
        except Exception as e:
            print(f"Error reading encrypted file: {e}")
            return {}

    def save(self):
        """Save the database to an encrypted file."""
        encrypted_data = self._encrypt_data(self.data)
        with open(self.file_path, 'w') as file:
            file.write(encrypted_data)

    def create_collection(self, collection_name):
        """Create a new collection."""
        if collection_name not in self.data:
            self.data[collection_name] = []
            self.save()
            return {"success": True, "message": f"Collection '{collection_name}' created successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' already exists."}

    def insert(self, collection_name, document):
        """Insert a document into a collection."""
        if collection_name in self.data:
            self.data[collection_name].append(document)
            self.save()
            return {"success": True, "message": "Document inserted successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def insert_many(self, collection_name, documents):
        """Insert multiple documents into a collection."""
        if collection_name in self.data:
            self.data[collection_name].extend(documents)
            self.save()
            return {"success": True, "message": "Documents inserted successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def find(self, collection_name, query=None):
        """Find documents in a collection."""
        if collection_name in self.data:
            if query:
                return [doc for doc in self.data[collection_name] if all(doc.get(k) == v for k, v in query.items())]
            return self.data[collection_name]
        else:
            print(f"Collection '{collection_name}' does not exist.")
            return []

    def find_by_field(self, collection_name, field, value):
        """Find documents by a specific field value."""
        if collection_name in self.data:
            return [doc for doc in self.data[collection_name] if doc.get(field) == value]
        else:
            print(f"Collection '{collection_name}' does not exist.")
            return []

    def update(self, collection_name, query, updates):
        """Update documents in a collection."""
        if collection_name in self.data:
            for doc in self.data[collection_name]:
                if all(doc.get(k) == v for k, v in query.items()):
                    doc.update(updates)
            self.save()
            return {"success": True, "message": "Documents updated successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def delete_one(self, collection_name, query):
        """Delete a single document from a collection."""
        if collection_name in self.data:
            for i, doc in enumerate(self.data[collection_name]):
                if all(doc.get(k) == v for k, v in query.items()):
                    self.data[collection_name].pop(i)
                    self.save()
                    return {"success": True, "message": "Document deleted successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def delete_many(self, collection_name, query):
        """Delete multiple documents from a collection."""
        if collection_name in self.data:
            self.data[collection_name] = [doc for doc in self.data[collection_name] if not all(doc.get(k) == v for k, v in query.items())]
            self.save()
            return {"success": True, "message": "Documents deleted successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def drop_collection(self, collection_name):
        """Remove a collection entirely."""
        if collection_name in self.data:
            del self.data[collection_name]
            self.save()
            return {"success": True, "message": f"Collection '{collection_name}' dropped successfully."}
        else:
            return {"success": False, "message": f"Collection '{collection_name}' does not exist."}

    def get_all_collections(self):
        """List all collections."""
        return list(self.data.keys())

    def get_all_documents(self):
        """Get all documents across collections."""
        return self.data

    def get_collection(self, collection_name):
        """Get a collection by its name."""
        if collection_name in self.data:
            return self.data[collection_name]
        else:
            return None
