
import random

def approximate_pi(n_terms):
    pi_estimate = 0
    for n in range(n_terms):
        pi_estimate += (-1)**n / (2 * n + 1)
    return 4 * pi_estimate

def estimate_pi(num_points):
    count_in_circle = 0
    radius = 0.5
    for _ in range(num_points):
        x = random.random()
        y = random.random()
        distance = ((x - radius)**2 + (y - radius)**2)**0.5
        if distance <= radius:
            count_in_circle += 1
    return 4 * count_in_circle / num_points

print(approximate_pi(10))
print(estimate_pi(10000))
