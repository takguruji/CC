x=2
learning_rate=0.2
iterations=100

for i in range(iterations):
    gradient = 2 * ( x + 3)
    x = x - learning_rate * gradient

y = (x+3)**2

print("Minimum x=" , round(x,4))
print("Minimum y=" , round(y,6))
