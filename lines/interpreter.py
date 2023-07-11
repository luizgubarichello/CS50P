expression = input("Expression: ").strip()

#COMENTARIO TESTE

x, y, z = expression.split(" ")

result = 0.0
if y == "+":
    result = int(x) + int(z)
elif y == "-":
    result = int(x) - int(z)
elif y == "*":
    result = int(x) * int(z)
elif y == "/":
    result = int(x) / int(z)

print(f"{result:.1f}")



#################



#

print ("a")