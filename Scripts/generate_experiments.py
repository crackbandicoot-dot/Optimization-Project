import json
import random
import numpy as np
# Configuration
output_path = '../Optimization-Project/Implementación/Experiments/exp1.json'
num_experiments = 300

# Parameter ranges
learning_rate_min = 0.01
learning_rate_max = 1
tol_min = 1e-7
tol_max = 1e-4
max_iter_min = 500
max_iter_max = 10000
x0_min = -100
x0_max = 100

def generate_experiments(num_experiments, lr_min, lr_max, tol_min, tol_max, iter_min, iter_max, x0_min, x0_max):
    experiments = []
    
    for _ in range(num_experiments):
        # Generate random learning rate (float)
        learning_rate = random.uniform(lr_min, lr_max)
        
        # Generate random tolerance in log space (to get powers of 10)
        tol_exp = random.uniform(int(np.log10(tol_min)), int(np.log10(tol_max)))
        tol = 10 ** random.uniform(tol_exp, tol_exp + 1)
        
        # Generate random max iterations (integer)
        max_iter = random.randint(iter_min, iter_max)
        
        # Generate random initial point
        x0 = [
            random.uniform(x0_min, x0_max),
            random.uniform(x0_min, x0_max)
        ]
        
        experiments.append({
            "learning_rate": round(learning_rate, 3),
            "tol": float(f"{tol:.1e}"),
            "max_iter": max_iter,
            "x0": [round(x, 2) for x in x0]
        })
    
    return experiments

# Generate the experiments
experiments = generate_experiments(
    num_experiments, learning_rate_min, learning_rate_max,
    tol_min, tol_max, max_iter_min, max_iter_max, x0_min, x0_max
)

# Save to JSON file
with open(output_path, 'w') as f:
    json.dump(experiments, f, indent=4)

print(f"Generated {num_experiments} experiments and saved to {output_path}")