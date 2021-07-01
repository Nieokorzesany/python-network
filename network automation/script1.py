import paramiko

username = ""
passwd=""
ip='192.168.1.21'
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username=username,password=passwd)
cmd="ls -ltr > test"

stdin,stdout,stderr=ssh_client.exec_command(cmd)
