# Core Pkgs
import numpy as np 
from memory_profiler import profile  



@profile(precision=2) 
def example_one():
	d = np.ones((100,1000,1000))
	return d 

# Save Output
fp = open("report_mem.log","w+")
@profile(stream=fp) 
def example_two():
	d = np.ones((100,1000,1000))
	s = sum(d)
	return s 




if __name__ == '__main__':
	example_one()
	example_two()

