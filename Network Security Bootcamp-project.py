import hashlib

password=hashlib.md5()

md_password=password.update('verysecretpassword'.encode())
#print md5 hash of password
print(password.hexdigest())

password=hashlib.sha1()
sha1_password=password.update('verysecretpassword'.encode())
#print sha1 hash of password
print(password.hexdigest())

password=hashlib.sha256()
sha1_password=password.update('verysecretpassword'.encode())
#print sha256 hash of password
print(password.hexdigest())

#adding salt

salt='!@#$'



passwd='verysecretpassword'+salt

salted=hashlib.md5(str.encode(passwd)).hexdigest()

print(salted)
#multiple hashed

twice=hashlib.md5(str.encode(salted)).hexdigest()
print(twice)

three=hashlib.md5(str.encode(twice)).hexdigest()
print(three)
four=hashlib.md5(str.encode(three)).hexdigest()

print(four)
