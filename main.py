from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

getFromDatabase_parser = reqparse.RequestParser()
getFromDatabase_parser.add_argument(
    "user_ID", type=str, help="ID of the user requesting", required=True)
getFromDatabase_parser.add_argument(
    "database_ID", type=str, help="database ID value")

user_database = {}


class GetFromDatabase(Resource):
    def post(self, user_ID, database_ID):
        return {"data": user_database}


api.add_resource(
    GetFromDatabase, "/getFromDatabase/<int:user_ID>/<int:database_ID>")

if __name__ == "__main__":
    app.run(debug=True)  # make sure to turn off during development
