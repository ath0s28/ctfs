from revenge import Process

#import process
p = Process("./beleaf",resume=False, verbose=False)
#postion address
mem = p.memory['beleaf:0x2014E0']
addr = mem.address
secuence = []
#size
for i in range(33):
    secuence.append(p.memory[addr + (i*8)].int64)
#letters address 
lookup = p.memory['beleaf:0x201020']
addr_fun = lookup.address

words = []
#2014df - 201020 = 0x4bf = 1215
#moving from DAT_00301020
for i in range(1215):
    # Function FUN_001007fa
    try:	
        # move 4 bits
        """
                
		long FUN_001007fa(char param_1)

		{
		  long local_10;
		  
		  local_10 = 0;
		  while ((local_10 != -1 && ((int)param_1 != *(int *)(&DAT_00301020 + local_10 * 4)))) {
		    if ((int)param_1 < *(int *)(&DAT_00301020 + local_10 * 4)) {
		      local_10 = local_10 * 2 + 1;
		    }
		    else {
		      if (*(int *)(&DAT_00301020 + local_10 * 4) < (int)param_1) {
			local_10 = (local_10 + 1) * 2;
		      }
		    }
		  }
		  return local_10;
		}
	

        """
        letter = p.memory[addr_fun + (i*4)].string_utf8
        words.append(letter)
    except Exception:
    	#exception utf8 ff
        words.append('f')	    
flag = ''
for n in secuence:
	flag = flag + words[n]
print(flag)
