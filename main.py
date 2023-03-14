import random
import sys

def estimate_pi(num_samples):
    num_points_in_circle = 0
    for i in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            num_points_in_circle += 1

    pi_estimate = 4 * num_points_in_circle / num_samples
    return pi_estimate, num_points_in_circle

if __name__ == '__main__':
    num_of_samples = int(sys.argv[1])
    pi_estimate, num_points_in_circle = estimate_pi(num_of_samples)
    
    print(f"Number of samples: {num_of_samples}")
    print(f"Number of points in circle: {num_points_in_circle}")
    print(f"PI estimate: {pi_estimate}")
