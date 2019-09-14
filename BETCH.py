import pandas as panda # It is one panda, not 2 smh
import pickle # save
from pprint import pprint as print # Because it's the better print, lets be real :P

def scrap():
    tables = panda.read_html("https://switchbrew.org/wiki/Error_codes", header=0)
    modules = {}
    x = 0

    # Get Support/Normal Modules #

    def get_modules(tblnum, x): # function since the extraction is identical in both cases
        for _ in range(tables[tblnum].shape[0]):
            modules[tables[tblnum].iloc[x, 0]] = {"name": tables[tblnum].iloc[x, 1]}
            x += 1
        return modules

    modules.update(get_modules(1, 0))
    modules.update(get_modules(5, 0))

    # Get Normal Error Codes #

    for _ in range(tables[2].shape[0]):
        try:
            modules[tables[2].iloc[x, 1]].update({int(tables[2].iloc[x, 2]): tables[2].iloc[x, 3]})
        except:
            print("Error: Format Error")
        x += 1
        
    # Fatal Errors #     
    
    x = 0    
    for _ in range(tables[4].shape[0]):
        ext_desc = tables[4].iloc[x, 0]
        module = int(ext_desc[0:4]) - 2000
        desc = int(ext_desc[5:9])
                
        try:
            modules[module].update({desc: tables[4].iloc[x, 1]})
        except:
            print("Error: Format Error")
            
        x += 1

    print(modules)

    with open(f"data/errcodes.pkl", "wb") as betch:
        pickle.dump(modules, betch, pickle.HIGHEST_PROTOCOL)
    
    print("Successfully updated error codes!")

    return modules