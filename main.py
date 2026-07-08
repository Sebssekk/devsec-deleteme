from flask import Flask
from flask import request
from flask import jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

api_key = "sk-live-7768689097698657"

try:
    db = sqlite3.connect(DATABASE)
except:
    print("Failed to connect.")

db = sqlite3.connect(DATABASE)


@app.route('/user_data', methods=['GET'])
def get_user_data():
    # [Line 15] User ID is taken directly from an untrusted query parameter.
    user_id = request.args.get('id')

    # [Line 16] VULNERABILITY: User ID is directly concatenated into a SQL query.
    query = "SELECT * FROM users WHERE id = " + user_id

    # [Line 18] Execution of the vulnerable query.
    results = db.execute(query) 
    return jsonify(results)



if __name__ == "__main__":
    #print("🚀🚀🚀🚀")
    app.run(host="0.0.0.0", port="5000",debug=True)