import telnetlib

host = '192.168.136.11'
user = 'python'
password = '123'

tn = telnetlib.Telnet(host)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b'Password: ')
tn.write(password.encode('ascii') +b'\n')

tn.write(b'config t\n')
tn.write(b'int loopback 1\n')
tn.write(b'ip address 1.1.1.1 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))
