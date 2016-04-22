max_value = int(raw_input("Enter the max. value in range: "))
total = sum(i for i in range(max_value) if (i%3==0 or i%5==0))
print total