import BETCH
import simplejson

if __name__ == "__main__":
    data = BETCH.scrap()
    
    with open("api.json", "w") as file:
        simplejson.dump(data, file, indent = 3, ignore_nan=True)