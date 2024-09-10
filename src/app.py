import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure('Jackson')

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

initial_members = [
    {'first_name': 'John', 'age': 33, 'lucky_numbers': [7, 13, 22]},
    {'first_name': 'Jane', 'age': 35, 'lucky_numbers': [10, 14, 3]},
    {'first_name': 'Jimmy', 'age': 5, 'lucky_numbers': [1]}
]

#for member in initial_members:
    #jackson_family.add_member(member)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify({
            "name": member["first_name"],
            "id": member["id"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }), 200
    else:
        return jsonify({"error": "member not found"}), 404

@app.route('/member', methods=['POST'])
def add_one_member():
    body = request.get_json()
    if not body or not all(k in body for k in ("first_name", "age", "lucky_numbers")):
        return jsonify({"error": "Invalid data"}), 400

    
    new_member = jackson_family.add_member(body)
    return jsonify(new_member), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(debug=True)
