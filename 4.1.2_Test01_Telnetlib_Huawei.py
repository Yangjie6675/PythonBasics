import telnetlib
import time

host = '192.168.136.16'
user = 'python'
password = '123'

tn = telnetlib.Telnet(host)

tn.read_until(b'Username:')
tn.write(user.encode('ascii') + b'\n')
tn.read_until(b'Password:')
tn.write(password.encode('ascii') +b'\n')

tn.write(b'system\n')
tn.write(b'int loopback 1\n')
tn.write(b'ip address 1.1.1.6 255.255.255.255\n')
tn.write(b'commit\n')
tn.write(b'return\n')

time.sleep(0.5)
tn.write(b'quit\n')

#print(tn.read_all().decode('ascii'))
print(tn.read_very_eager().decode('ascii'))
