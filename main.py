from flask import Flask
from flask_restful import Resource, Api
from controllers.company import *
from controllers.collaborator import *

app = Flask(__name__)
api = Api(app)

    
    
api.add_resource(Companies, '/companies')
api.add_resource(Company, '/companies/<string:id>')

if __name__ == '__main__':
   app.run(debug=True)