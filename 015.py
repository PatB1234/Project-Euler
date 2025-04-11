# Apporach uses combinatrics (Binomial coefficient)
import math

grid_x = 20
grid_y = 20

n = grid_x + grid_y
k = grid_y

NPaths = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(int(NPaths))