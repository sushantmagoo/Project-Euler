# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def euler3(n):
    while n % 2 == 0 and n != 2:
    	n = n/2
    i = 3
    while i < n ** 0.5:
        if n % i == 0:
            n = n / i
        i = i + 2
    return n
            
if __name__ == "__main__":

	print euler3(600851475143)