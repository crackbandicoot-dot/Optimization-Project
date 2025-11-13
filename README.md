# Optimization Project: Arctan Function Minimization

## Objective Function
f(x,y) = -arctan(x+y+1) - arctan(x-y+2) - arctan(-x-y+3) - arctan(-x+y+4)

## Project Structure
- `Informe.pdf`: Theoretical analysis and mathematical foundations
- `Implementación/`: Python implementation and experiments
  - `Implementación_Métodos.ipynb`: Main notebook with optimization methods
  - `Experiments/`: JSON configuration files for experiments
  - `Results/`: Output results from experiments

## Requirements
- Python 3.7+
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

## Installation
```bash
pip install numpy scipy matplotlib jupyter
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook Implementación/Implementación_Métodos.ipynb
```

2. Run all cells to execute the optimization methods

3. Experiments are automatically loaded from `Experiments/` folder and results saved to `Results/`

## Methods Implemented
- Gradient Descent with configurable learning rate
- Quasi-Newton BFGS method

## Experiments
Configure experiments by creating JSON files in `Experiments/` folder with parameters:
- `learning_rate`: Step size for gradient descent
- `tol`: Convergence tolerance
- `max_iter`: Maximum iterations
- `x0`: Initial point [x, y]