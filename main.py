from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return{"1" : "Hello World"}
    
    def post(self):
        return{"1" : "This is a post call"}
        
class Sum(Resource):
    def post(self):
        data = request.get_json()
        num1 = data.get('num1')
        num2 = data.get('num2')
        total = num1 + num2
        return {"sum": total}

api.add_resource(HelloWorld, "/")
api.add_resource(Sum, "/sum")

if (__name__ == "__main__"):
    app.run(debug=True)