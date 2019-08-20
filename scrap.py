import pandas as panda # It is one panda, not 2 smh
import pprint

tables = panda.read_html("https://switchbrew.org/wiki/Error_codes", header=0)

def conv(tblnum, y, z): # y = 1st col, z = 2nd col
    rows = tables[tblnum].shape[0] # Shape = = | &!= -
    x = 0
    varform = {}

    print(rows)
    for _ in range(rows):
        varform.update({tables[tblnum].iloc[x, y]: tables[tblnum].iloc[x, z]})
        x += 1

    pprint.pprint(varform)
    return varform

modules = conv(1, 0, 1)
modules.update(conv(5, 0, 1)) # Support modules
errcodes = conv(2, 0, 3)