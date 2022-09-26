from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import json
from models.data import *
from controllers.company import *

class Collaborator(Resource):
    
    #get collaborator in enterprise args
    def get(self, name):
        data = []
        for collab in enterprises:
            if collab['name'] == name:
                return collab
        return None

    def delete(self, name):
        global enterprises
        enterprises = [enterprise for enterprise in enterprises if enterprise['name'] != name] #list comprehension
        return make_response(jsonify(enterprises), 200)
    
        