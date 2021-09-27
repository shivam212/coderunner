from flask import Flask
from flask_restful import reqparse, Resource, Api
from runner import coderunnerPython, coderunnerCPP

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('code')
parser.add_argument('input')

class codeRunnerPython(Resource):
    def get(self):
        return {"working":"working"}
    def post(self):
        args = parser.parse_args()
        code = args['code']
        input = args['input']
        with open('code_to_run.py', mode='w') as f:
            f.write(code) 
        output = coderunnerPython(input) 
        return {"args":args, "output":output[1], "compile": output[0]}

class codeRunnerCPP(Resource):
    def get(self):
        return {"working":"working"}
    def post(self):
        args = parser.parse_args()
        code = args['code']
        input = args['input']
        with open('code_to_run.cpp', mode='w') as f:
            f.write(code) 
        output = coderunnerCPP(input) 
        return {"args":args, "output":output[1], "compile": output[0]}
 
api.add_resource(codeRunnerPython,'/python')
api.add_resource(codeRunnerCPP,'/cpp')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", debug=True)
