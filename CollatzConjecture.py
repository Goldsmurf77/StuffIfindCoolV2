import matplotlib.pyplot as plt

x = int(input("what will be the number?"))
num = int(1)
pointsx = []
numy = []
y = 0
z = 0
if x == 2:
    y = 0
elif x % 2 == 0:
    y = y + 1
else:
    z = z + 1

pointsx.append(x)
numy.append(num-1)
while x>1:
    if x%2==0:
        x = x//2
        num = num + 1
        pointsx.append(x)
        numy.append(num)
        y = y+1
        print("it was divided by 2")
        
    else:
        x = x*3+1
        num = num + 1
        pointsx.append(x)
        numy.append(num)
        z = z + 1
        print("it was odd")

print("your num lasted",num,"amount of times, YAY")  
print("your num was divided by 2",y,"times")
print("your num was 3x+1",z,"times")
plt.plot(numy,pointsx)
plt.xlabel("Num you input")
plt.ylabel("Times it happend")
plt.show()
