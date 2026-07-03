import math
def generate_fractions(n):
	res = []
	curr = 1
	
	while curr < n:
	  for i in range(2, n + 1):
	    if curr / i >= 1:
	      continue
	    
	    else:
	      if math.gcd(curr, i) == 1:
	        res.append([curr, i])
	  
	  curr += 1
	 
	return res
