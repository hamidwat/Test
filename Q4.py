# This code calculates the fibonacci series via a recursive algorithm.
# To speed up the algorithm, values are restored in a dictionary to avoid extra calculations later

import time

saved_results = {}
def fibonacci(n):
	# Make sure that n is a non-negative integer	
	if type(n) != int:
		raise TypeError('n must be a non-negative int')
	if n<0:
		raise ValueError('n must be a non-negative int')
	
	# If fibonacci(n) was calcaulated before, then return it without any extra calculation
	if n in saved_results:
		return saved_results[n]
	
	# Calculation of the n-th term
	if n==0:
		result = 0
	elif n==1:
		result = 1
	elif n>1:
		result = fibonacci(n-1) + fibonacci(n-2)
	
	# Save the value of fibonacci(n) and return it	
	saved_results[n] = result
	return result

start_time = time.time()
for i in range(101):
	# Elapsed time from the beginning is shown in brackets
	print('fibonacci({}):{}    [{:.8f}ms]'.format(i, fibonacci(i), (time.time() - start_time)*1000))
#


