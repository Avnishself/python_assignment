# fibonacci sequence program

def fibon(n):
   
   if n <= 1:
       return n
   else:
       return(fibon(n-1) + fibon(n-2))


# input from the user
num = int(input("Enter numbers for generate sequence? "))

# check if the number of terms is valid
if num <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(num):
       print(fibon(i))
