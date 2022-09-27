from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import json
from models.data import *

ITEM_NOT_FOUND = 'Item not found'

class Collaborators(Resource):
    def get(self):
        return enterprises   

    
class Collaborator(Resource):
    
    args = reqparse.RequestParser()
    args.add_argument('id')    
    args.add_argument('business')
    args.add_argument('name')
    args.add_argument('email')
    
    
    def find_enterprise(business):
        for enterprise in enterprises:
            if enterprise['business'] == business:
                return enterprise
        return None
    
    def get(self, business):     #listar dados de uma empresa    
        enterprise = Collaborator.find_enterprise(business)
        new_data = []
        
        for enterprise in enterprises:
            if enterprise['business'] == business:
                new_data.append(enterprise)
        return new_data    
        

        
class Del_Collaborator(Resource):
    def delete(self, name):
        global enterprises
        enterprises = [enterprise for enterprise in enterprises if enterprise['name'] != name] #list comprehension
        return make_response(jsonify(enterprises), 200)