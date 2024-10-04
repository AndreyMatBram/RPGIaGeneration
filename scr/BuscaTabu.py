"""
Tabu Search Algorithm
This script implements the Tabu Search algorithm to find the best solution for a given problem. The algorithm iteratively explores the neighborhood solutions and keeps track of the best solution found so far. It uses a tabu list to prevent revisiting previously explored solutions.
Functions:
- evaluate(solution): Evaluates the fitness of a given solution.
- tabu_search(initial_solution, tabu_list_size, num_iterations): Executes the Tabu Search algorithm.
- generate_neighborhood(solution): Generates the neighborhood solutions for a given solution.
Usage:
1. Define the initial solution.
2. Define the tabu list size and the number of iterations.
3. Run the Tabu Search algorithm by calling the tabu_search() function.
4. The best solution and its evaluation will be returned.
Example:
initial_solution = [1, 50, 26, 25, 1]
best_solution, best_evaluation = tabu_search(initial_solution, tabu_list_size, num_iterations)
"""

from EvoBattle import evolution
import numpy as np

plystts = [12,32,25,21,14]
levelCap = sum(plystts[:5])

def evaluate(solution):
    iastts = solution[:5]
    a = evolution(iastts, plystts, levelCap)
    return a

# Define the Tabu Search function
def tabu_search(initial_solution, tabu_list_size, num_iterations):
    current_solution = initial_solution.copy()
    best_solution = initial_solution.copy()
    best_evaluation = evaluate(best_solution)

    # Initialize the tabu list as a set for efficient lookups
    tabu_list = set()

    # Start the iterations
    for _ in range(num_iterations):
        # Generate the neighborhood solutions
        neighborhood_solutions = generate_neighborhood(current_solution)
    
    # Evaluate the neighborhood solutions
    for solution in neighborhood_solutions:
        # Convert the solution to a tuple for set operations
        solution_tuple = tuple(solution)
        if solution_tuple not in tabu_list:
            current_evaluation = evaluate(solution)
            if current_evaluation > best_evaluation:
                best_solution = solution.copy()
                best_evaluation = current_evaluation
    
    # Update the tabu list
    tabu_list.add(tuple(current_solution))
    if len(tabu_list) > tabu_list_size:
        # Remove the oldest element from the set
        tabu_list.pop()
    
    # Move to the best solution found in the neighborhood
    current_solution = best_solution.copy()
    
    return best_solution, best_evaluation

# Define the function to generate neighborhood solutions
def generate_neighborhood(solution):
    neighborhood_solutions = []
    
    # Generate all possible neighbor solutions by changing one number at a time
    for i in range(len(solution)):
        for j in range(1, 10):
            neighbor_solution = solution.copy()
            neighbor_solution[i] = j
            neighborhood_solutions.append(neighbor_solution)
    
    return neighborhood_solutions

# Define the initial solution
initial_solution = np.random.randint(int(levelCap/5), int(levelCap/5)*2, 5)

# Define the tabu list size and number of iterations
tabu_list_size = 100
num_iterations = 5000

# Run the Tabu Search algorithm
best_solution,best_evaluation = tabu_search(initial_solution, tabu_list_size, num_iterations)

# Print the best solution
print("Melhor solução:", best_solution)
print("Vida Restante:", best_evaluation)
