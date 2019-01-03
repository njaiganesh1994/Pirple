#Initialization of counter for prime number check
#For loop for 1 to 100
for i in range(1,101):
	num1=0
	#Divisibility check for 3 and 5
	if i%3==0 and i%5==0:
		print("FizzBuzz")
		continue
	#Divisibility check for 3
	if i%3==0:
		print("Fizz")
		continue
	#Divisibility check for 3 and 5
	if i%5==0:
		print("Buzz")
		continue
	#Prime Number Check
	for n in range(1,i+1):
		if i%n==0 and i>1 and n>1:
			num1=num1+1	
	if num1==1:
		print("Prime")
		continue
	else:
		print(i)
i=i+1
