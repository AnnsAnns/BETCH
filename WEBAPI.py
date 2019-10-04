import BETCH
import hug

@hug.get("/API/BETCH/ERRCODE")
def betch_api(module_int: int, description_int: int):
    modules = BETCH.load()
    
    response = {"module_int": module_int, 
                "module_name": "Unknown",
                "description_int": description_int,
                "description_str": "Unknown"}
    
    if module_int in modules:
        if "name" in modules[module_int]:
            response["module_name"] = modules[module_int]["name"]
        if description_int in modules[module_int]:
            response["description_str"] = modules[module_int][description_int]
    
    return response

@hug.get("/API/BETCH/ALL")
def all_errorcodes():
    modules = BETCH.load()    
    return modules