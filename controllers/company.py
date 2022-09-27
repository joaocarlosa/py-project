from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import json
from models.data import *

ITEM_NOT_FOUND = 'Item not found'

class Companies(Resource):
    def get(self):
        return enterprises
    
class Company(Resource):
    
    args = reqparse.RequestParser()
    args.add_argument('id')
    args.add_argument('business')
    args.add_argument('name')
    args.add_argument('email')
    args.add_argument('role')
    args.add_argument('manager')
    
    
    def find_enterprise(id):
        for enterprise in enterprises:
            if enterprise['id'] == id:
                return enterprise
        return None
    
    def get(self, id):        
        enterprise = Company.find_enterprise(id)
        if enterprise:
            return enterprise        
        return {'message': ITEM_NOT_FOUND}, 404  
    
    def post(self, id):      
        data = Company.args.parse_args()
        new_data = {**data}
        enterprises.append(new_data) 
        #new_data = HotelModel(**data)
        return enterprises, 201
        #return enterprises, 201
        
    def put(self, id):
        data = Company.args.parse_args()        
        new_data = {**data}
        enterprise = Company.find_enterprise(id)
        if enterprise:
            enterprise.update(new_data)
            return new_data, 202
        enterprises.append(new_data)
        
        new_data = HotelModel(**data)
        return new_data, 201 #created
        
    def delete(self, id):
        global enterprises
        enterprises = [enterprise for enterprise in enterprises if enterprise['id'] != id] #list comprehension
        return make_response(jsonify(enterprises), 200)