import json

friends={"Dan":[20,"London",1234141],"Maria":[25,"Madrid",12312431]}

with open('friends.json','w') as f:
    json.dump(friends,f)
    
with open('friends.json','r') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

with open('friends.json.','w') as f:
    json.dump(friends,f,indent=4)

json_string=json.dumps(friends,indent=4)
print(json_string)