from flask import Flask
from flask_restful import Resource, Api
from controllers.company import *
from controllers.collaborator import *
from controllers.organograma import orgranograma

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Companies, '/companies')
api.add_resource(Company, '/companies/<string:id>')

api.add_resource(Collaborators, '/collaborators')
api.add_resource(Collaborator, '/collaborator/<string:business>')
api.add_resource(Del_Collaborator, '/collaborator/<string:name>')

api.add_resource(orgranograma, '/organograma/<string:name>')

if __name__ == '__main__':
   app.run(debug=True)