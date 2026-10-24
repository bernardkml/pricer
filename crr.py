import math

S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.2
N = 3
dt = T/N
u = math.exp(sigma * math.sqrt(dt))
d = 1/u
p = (math.exp(r*dt)-d)/(u - d)

print("dt=",dt)
print("u=",u)
print("d=",d)
print("p=",p)
