import BETCH

from flask import Flask, request
from flask_restful import Resource, Api
from config import force_reload_token

modules = BETCH.load()
app = Flask(__name__)
api = Api(app)

class BETCH_api(Resource):
    def get(self, module_int, description_int):
        module_int = int(module_int)
        description_int = int(description_int)
        
        response = {"module_int": module_int, 
                "module_str": "Unknown",
                "description_int": description_int,
                "description_str": "Unknown"}
    
        if module_int in modules:
            if "name" in modules[module_int]:
                response["module_str"] = modules[module_int]["name"]
            if description_int in modules[module_int]:
                response["description_str"] = modules[module_int][description_int]
        
        return response

class All(Resource):
    def get(self):
        return modules

class Reload(Resource):
    def get(self, token):
        global modules
        
        if token == force_reload_token:
            modules = BETCH.scrap()
            return "Reloading :)"
        
        return "Wrong token!"
            
api.add_resource(BETCH_api, "/api/betch/<module_int>/<description_int>")
api.add_resource(All, "/api/betch/all")
api.add_resource(Reload, "/api/betch/reload/<token>")

app.run(port="80")