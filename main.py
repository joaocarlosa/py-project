from flask import Flask
from flask_restful import Resource, Api
from controllers.company import *
from controllers.collaborator import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all( )
    
    
api.add_resource(Companies, '/companies')
api.add_resource(Company, '/companies/<string:id>')
api.add_resource(Collaborator, '/collaborator/<string:business>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app) #garante que o banco nao seja executado de outro arquivo
    app.run(debug=True)