from Contract_Functions import web3_init, getNames, getSharedImages, shareImage, doesUserExist, grantAccess, revoke_access, registerUser, getAllUsers
from Construct_Merkle_Tree import merkle_tree_construction_driver
from flask import Flask, jsonify, request

import json
import os
from dotenv import load_dotenv

load_dotenv()

contract_address = os.getenv("CONTRACT_ADDRESS")
infura_project_id = os.getenv("INFURA_PROJECT_ID")
infura_endpoint = os.getenv("INFURA_ENDPOINT")
acct_private_key = os.getenv("ACCT_PRIVATE_KEY")

with open("Contract.json") as f:
    info_json = json.load(f)
abi = info_json["abi"]


app = Flask(__name__)

web3, contract = web3_init(
    infura_endpoint, infura_project_id, abi, contract_address)


@app.route('/<user>/communications')
def users_list(user):
    users_communicated_with = getNames(contract, acct_private_key, user)

    try:

        user_list = []
        print(users_communicated_with)
        for i in range(len(users_communicated_with)):
            user_list.append({
                "firstName": users_communicated_with[i][0],
                "lastName": users_communicated_with[i][1],
                "email": users_communicated_with[i][2]
            })

        return jsonify(user_list)
    except:
        return jsonify({"status_code": 406, "message": "Unexpected error"})


@app.route('/users')
def all_users_list():
    users = getAllUsers(contract)

    try:

        all_user_list = []
        print(users)
        for i in range(len(users)):
            all_user_list.append({
                "firstName": users[i][0],
                "lastName": users[i][1],
                "email": users[i][2]
            })

        return jsonify(all_user_list)

    except:
        return jsonify({"status_code": 406, "message": "Unexpected error"})


@app.route('/<user1>/communications/<user2>')
def images_shared(user1, user2):
    images_shared = getSharedImages(contract, acct_private_key, user1, user2)
    print(images_shared[1])
    imgs_shared_arr = []
    for i in images_shared[1]:
        imgs_shared_arr.append({
            "merkle_hash": i[0],
            "url": i[1],
            "timestamp": i[2],
            "caption": i[3],
            "hasAccess": i[4],
            "is_Sender": i[5]

        })

    return jsonify(imgs_shared_arr)


@app.route('/<user1>/communicate/<user2>', methods=['POST'])
def share(user1, user2):

    try:
        if(doesUserExist(contract, user2) == 0):
            return jsonify({"status_code": 406, "message": "User not found"})
        url = request.json['url']
        image_hash = merkle_tree_construction_driver(url)
        print(image_hash)
        time_stamp = request.json['time_stamp']
        caption = request.json["caption"]
        returned_val = {'data': {"user1": user1, "user2": user2, "url": url,
                                    "time_stamp": time_stamp, "image_hash": image_hash, "caption": caption}}
        try:
            shareImage(web3, contract, acct_private_key,
                        user1, user2, url, image_hash, time_stamp, caption)
            return jsonify(returned_val), 201
        except:
            return jsonify({"status_code": 406, "message": "Unexpected error"})
    except:
        return jsonify({"status_code": 406, "message": "Incorrect input"})


@app.route("/<user>/access", methods=["POST"])
def access_modifier(user):

    try:
        sender = user
        receiver = request.json["user2"]
        idx = request.json["idx"]
        type = request.json["access_type"]
        result = ""
        try:
            if(type == "grant"):
                result = grantAccess(
                    web3, contract, acct_private_key, receiver, sender, idx)
                print("on grant, result:", result)
                result = result['status']
            else:
                result = revoke_access(
                    web3, contract, acct_private_key, sender, receiver, idx)
                print("on revoke,result:", result)
                result = result['status']

        except:
            return jsonify({"msg": "oops"})

        if(result == 0):
            return jsonify({"status_code": 406, "message": "Failed as you do not have access"})
        elif (result == 1):
            return jsonify({"status_code": 200, "message": "success"})
    except:
        return jsonify({"status_code": 500, "message": "unexpected error"})


@app.route("/register", methods=["POST"])
def register():
    userName = request.json["email"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    try:
        registerUser(web3, contract, acct_private_key,
                     userName, firstName, lastName)
        return jsonify({"status_code": 201, "data": {
            "firstName": firstName,
            "lastName": lastName,
            "email": userName
        }})

    except:
        return jsonify({"status_code": 406, "message": "Unexpected Error"})
