#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

max_value = int(raw_input("Enter the max. value for range: "))
total = sum(i for i in range(max_value) if (i%3==0 or i%5==0))
print total