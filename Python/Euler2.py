# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

prev, curr = 0, 1
total = 0
while curr < 4000000:
	if curr % 2 == 0:
		total += curr
	prev, curr = curr, prev+curr
print total