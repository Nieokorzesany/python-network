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
    command = 'sudo cat /etc/shadow\n'
    (stdin, stdout, stderr) = ssh_client.exec_command(command, get_pty=True)

    cmd_output = stdout.read()
    print(command, cmd_output.decode('utf-8'))


    ssh_client.close()

for idx,server in enumerate(server):
    try:
        print('server number {}'.format(idx))
        server_exec(server)
    except TimeoutError:
        print("server {} is down".format(idx))