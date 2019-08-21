import pandas as panda # It is one panda, not 2 smh
import pickle # save
from pprint import pprint as print # Because it's the better print, lets be real :P

def scrap():
    tables = panda.read_html("https://switchbrew.org/wiki/Error_codes", header=0)
    modules = {}
    x = 0

    def get_modules(tblnum, x):
        for _ in range(tables[tblnum].shape[0]):
            modules[tables[tblnum].iloc[x, 0]] = {"name": tables[tblnum].iloc[x, 1]}
            x += 1
        return modules

    modules.update(get_modules(1, 0))
    modules.update(get_modules(5, 0))

    for _ in range(tables[2].shape[0]):
        try:
            modules[tables[2].iloc[x, 1]].update({int(tables[2].iloc[x, 2]): tables[2].iloc[x, 3]})
        except:
            print("Error: Format Error")
        x += 1

    print(modules)

    with open(f"data/errcodes.pkl", "wb") as betch:
        pickle.dump(modules, betch, pickle.HIGHEST_PROTOCOL)
    
    print("Successfully updated error codes!")

    return modules