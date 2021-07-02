import paramiko
import time
import json

server={}
with open('server.json','r') as f:
    server = json.load(f)



ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(**server,look_for_keys=False,allow_agent=False)
shell=ssh_client.invoke_shell()
shell.send('uname -a\n')
time.sleep(1)
output=shell.recv(100).decode('utf-8')
print(output)
#cmd="ls -ltr > test"

#stdin,stdout,stderr=ssh_client.exec_command(cmd)



ssh_client.close()