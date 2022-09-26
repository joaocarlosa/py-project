from flask import Flask
from flask_restful import Api, Resource
from instance import server

app, api = server.app, server.api

books_db = [
    {'id' : 0, 'title' : 'Clean Code' },
    {'id' : 1, 'title' : 'Design Patterns' },
]

class BookList(Resource):
    def get(self, ):
        return books_db