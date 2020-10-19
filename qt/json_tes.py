import json
Dict = {"name":"tom"}
c = json.dumps(Dict)
with open("./file.json", "w") as f:
    f.write(c)