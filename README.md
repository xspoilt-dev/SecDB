# SecDB

**SecDB** is a secure, lightweight, and document-based NoSQL database for Python applications. It supports AES-256-CBC encryption for secure data storage and provides a server-client architecture for easy interaction.

---

## Features

- **Encryption:** AES-256-CBC with SHA-256 for key derivation.
- **NoSQL:** Document-based storage for flexible data management.
- **Server-Client Architecture:** Interact with the database securely through REST APIs.
- **Customizable:** Configure database name, password, and server URLs.

---

## Requirements

- Python 3.8+
- Required libraries: 
  - `flask`
  - `requests`
  - `pycryptodome`

Install the dependencies using:

```bash
pip install flask requests pycryptodome
git clone https://github.com/xspoilt-dev/SecDB.git
cd SecDB
python server.py
```
## Using `client.py`

After importing `client.py` into your Python script, you can use its functions to interact with the SecDB server. Below are examples of how to use each method.

### Setup
Ensure that the `SERVER_URL` is correctly set in the `client.py` file to point to your SecDB server:
```python
SERVER_URL = "http://your-server-address:port"
```

---

### Example Usage

1. **Import the `client.py` file**  
   ```python
   import client
   ```

2. **Create a Collection**  
   ```python
   response = client.create_collection("users")
   print(response)  # {'message': "Collection 'users' created.", 'success': True}
   ```

3. **Insert a Single Document**  
   ```python
   document = {"name": "Alice", "age": 25}
   response = client.insert_document("users", document)
   print(response)  # {'affected_count': 1, 'success': True}
   ```

4. **Insert Multiple Documents**  
   ```python
   documents = [
       {"name": "Bob", "age": 30},
       {"name": "Charlie", "age": 35}
   ]
   response = client.insert_many_documents("users", documents)
   print(response)  # {'affected_count': 2, 'success': True}
   ```

5. **Find Documents**  
   ```python
   query = {"age": 25}
   response = client.find_documents("users", query)
   print(response)  # {'count': 1, 'result': [{"name": "Alice", "age": 25}], 'success': True}
   ```

6. **Find by Field**  
   ```python
   response = client.find_by_field("users", "name", "Alice")
   print(response)  # {'count': 1, 'result': [{"name": "Alice", "age": 25}], 'success': True}
   ```

7. **Get All Collections**  
   ```python
   response = client.get_all_collections()
   print(response)  # {'result': ['users'], 'success': True}
   ```

8. **Get All Documents**  
   ```python
   response = client.get_all_documents()
   print(response)  # {'result': {'users': [...]}, 'success': True}
   ```

9. **Update Documents**  
   ```python
   query = {"name": "Alice"}
   updates = {"age": 26}
   response = client.update_documents("users", query, updates)
   print(response)  # {'affected_count': 1, 'success': True}
   ```

10. **Delete a Single Document**  
    ```python
    query = {"name": "Alice"}
    response = client.delete_one_document("users", query)
    print(response)  # {'affected_count': 1, 'success': True}
    ```

11. **Delete Multiple Documents**  
    ```python
    query = {"age": {"$gte": 30}}
    response = client.delete_many_documents("users", query)
    print(response)  # {'affected_count': 2, 'success': True}
    ```

12. **Drop a Collection**  
    ```python
    response = client.drop_collection("users")
    print(response)  # {'message': "Collection 'users' dropped.", 'success': True}
    ```

---

### Customization
- **Set Database Name and Password**  
  Update the database name or password in your server (`server.py`) setup to secure your data.
- **Change Server URL**  
  Set the `SERVER_URL` in `client.py` to point to your SecDB server's address.

With these examples, users can easily integrate SecDB into their Python applications.
