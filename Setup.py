import random
import matplotlib.pyplot as plt
import Perceptron

p = [[-10, 5], [8, 16], [8, -5], [6, 4], [-5, 3], [-3, 4], [4, 2], [-5, -10],[2.5,10],[5,-5],[0,-5],[0,10]]
t = [1, 1, 0, 0, 1, 1, 0, 0,1,0,0,1]
temp = 0
w1 = random.uniform(0, 1)
w2 = random.uniform(0, 1)
b = random.uniform(0, 1)
a = 0
for x in p:
    (a,w1,w2,b)=Perceptron.learn(x[0], x[1], t[temp], w1, w2, b)
    if t[temp]==1:
        plt.scatter(x[0], x[1], label= "stars", color= "green")
    else:
        plt.scatter(x[0], x[1], label="stars", color="blue")
    print(a,w1,w2,b)
    temp = temp + 1


x=[]
y=[]
for i in (-10,10):
    x.append(i)
    y.append((-((b//w1)/(b//w2)))*i+(-b//w1))
plt.plot(x,y,color="red")
plt.show()
print(p)

#
