import math

def square_rooted (x):
    return math.sqrt(sum(xi * xi for xi in x))

def euclidean (x, y):
    return math.sqrt(sum((xi - yi) * (xi - yi)) for xi, yi in zip(x, y))

def manhattan (x, y):
    return sum(abs(xi - yi) for xi, yi in zip(x, y))

def cosine (x, y):
    numerator = sum(xi * yi for xi, yi in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)

    return numerator / denominator 

def pearson (x, y):
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_sq = sum(xi * xi for xi in x)
    sum_y_sq = sum(yi * yi for yi in y)
    
    p_sum = sum(xi * yi for xi, yi in zip(x, y))

    numerator = p_sum - (sum_x * sum_y / len(x))   
    denominator = math.sqrt((sum_x_sq - sum_x * sum_x / len(x)) * (sum_y_sq - sum_y * sum_y / len(y)))

    return (1.0 - numerator / denominator) if denominator else 0


