# + , - , * , /
expression = input("please enter ....") # 7 + 9
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
  print(x + z)
elif y == "-":
  print(x - z)
