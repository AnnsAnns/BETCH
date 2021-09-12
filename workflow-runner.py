import BETCH
import json

if __name__ == "__main__":
    data = BETCH.scrap()
    
    with open("api.json", "w") as file:
        json.dump(data, file, indent = 3)