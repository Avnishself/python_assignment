num1 = int(input("enter start range number: "))
num2 = int(input("enter end range number: "))

for num in range(num1,num2 +1):

  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      print(num)
