import paramiko
import time
import json

server=[]
with open('server.json','r') as f:
    server = json.load(f)

def connect(server_ip,server_port,user,password):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip,port=server_port,username=user,password=password,look_for_keys=False,allow_agent=False)

    return ssh_client

def get_shell(ssh_client):
    shell=ssh_client.invoke_shell()

    return shell

def send_command(shell,command,timeout=1):
    print(f'sending command{command}')
    shell.send(command+'\n')
    time.sleep(timeout)

def show(shell,n=1000000):
    output=shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active()==True:
        print('closing the connection')
        ssh_client.close()



client=connect(server[0]['hostname'],server[0]['port'],server[0]['username'],server[0]['password'])
shell=get_shell(client)

send_command(shell,'ls')
send_command(shell, 'ip a')

output=show(shell)
print(output)