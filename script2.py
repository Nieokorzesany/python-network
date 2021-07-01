import pickle

friends={"Dan":[20,"London",1234141],"Maria":[25,"Madrid",12312431]}

with open('friends.dat','wb') as f:
    pickle.dump(friends,f)

with open('friends.dat','rb') as f:
    obj = pickle.load(f)
    print(obj)