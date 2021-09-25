from flask import Flask
from flask_restful import reqparse, Resource, Api
from runner import coderunner

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('code')
parser.add_argument('input')

class codeRunner(Resource):
    def get(self):
        return {"working":"working"}
    def post(self):
        args = parser.parse_args()
        code = args['code']
        input = args['input']
        with open('code_to_run.py', mode='w') as f:
            f.write(code) 
        output = coderunner(input) 
        print(output)
        return {"args":args, "output":output}

api.add_resource(codeRunner,'/')

if __name__ == '__main__':
    app.run(debug=True)
