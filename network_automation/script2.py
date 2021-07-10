import paramiko
import time
import json

server=[]
with open('server.json','r') as f:
    server = json.load(f)

def server_exec(server):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**server,look_for_keys=False,allow_agent=False)
    stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)

    stdin.write(server["password"]+'\n')  # this is the sudo password
    time.sleep(2)  #waiting for the remote server to finish

    stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
    print(stdout.read().decode())
    time.sleep(1)

for idx,server in enumerate(server):
    try:
        print('server number {}'.format(idx))
        server_exec(server)
    except TimeoutError:
        print("server {} is down".format(idx))