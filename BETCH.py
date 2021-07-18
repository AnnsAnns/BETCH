# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pandas as panda # It is one panda, not 2 smh
import pickle # save
from pprint import pprint as print # Because it's the better print, lets be real :P
from data.legacy_errcodes import switch_support_page, special_err

def load():
    with open(f"data/errcodes.pkl", "rb") as betch:
        errcodes = pickle.load(betch)
    print("Error codes have been loaded!")
    return errcodes

def dump(data):
    with open(f"data/errcodes.pkl", "wb") as betch:
        pickle.dump(data, betch, pickle.HIGHEST_PROTOCOL)
    print("Error codes have been dumped!")

# Simplify code and have easier edge case protection
def updatedict(module, desc, str_desc):
    global modules
    
    if not module in modules:
        modules[module] = {}

    try:
        modules[module].update({desc: str_desc})
    except:
        print("Error updating error (Ironic, isn't it)")

def scrap_fatal(x):
    for _ in range(tables[4].shape[0]):
        ext_desc = tables[4].iloc[x, 0]
        module = int(ext_desc[0:4]) - 2000
        desc = int(ext_desc[5:9])

        try:
            updatedict(module, desc, tables[4].iloc[x, 1])
        except:
            print("Error: Format Error")
        x += 1

def scrap_normal(x):
    for _ in range(tables[2].shape[0]):
        try:
            updatedict(int(tables[2].iloc[x, 1]), int(tables[2].iloc[x, 2]), tables[2].iloc[x, 3])
        except:
            print("Error: Format Error")
        x += 1

def scrap_modules(x, tblnum): # function since the extraction is identical in both cases
    for _ in range(tables[tblnum].shape[0]):
        updatedict(int(tables[tblnum].iloc[x, 0]), "name", tables[tblnum].iloc[x, 1])
        x += 1
            
def scrap_fs(x):
    for _ in range(tables[3].shape[0]):
        try: # FS errors are the ranged error heaven so we can only scrap a very small amount without handling edge cases
            err = tables[3].iloc[x, 0][2:]
            errcode = int(err, 16)
            desc = (errcode >> 9) & 0x3FFF

            updatedict(2, desc, tables[3].iloc[x, 2])
        except:
            print("Error: Format Error")
        x += 1

def scrap_legacy_converter():
    # Nintendo's official error pages #
    
    for err in switch_support_page.keys():
        module = int(err[0:4]) - 2000
        desc = int(err[5:9])
        
        updatedict(module, desc, switch_support_page[err])
    
    # Special/Non-Switchbrew Error Codes #
    
    for oerr in special_err.keys():
        err = oerr[2:]
        errcode = int(err, 16)
        module = errcode & 0x1FF
        desc = (errcode >> 9) & 0x3FFF
        
        updatedict(module, desc, special_err[oerr])
    
def scrap():
    global modules
    global tables
    
    modules = {}
    tables = panda.read_html("https://switchbrew.org/wiki/Error_codes", header=0)    
    
    scrap_modules(0, 1) # Normal Modules
    scrap_modules(0, 5) # Support Modules
    scrap_modules(0, 7) # Homebrew Modules
    
    scrap_legacy_converter()
    scrap_fatal(0)
    scrap_fs(0)
    scrap_normal(0)

    print(modules)
    dump(modules)

    print("Successfully updated error codes!")

    return modules

if __name__ == "__main__":
    scrap()