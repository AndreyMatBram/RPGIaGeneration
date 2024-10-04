import random

# Define the evaluation function
def evaluate(solution):
    # Exemplo de função de avaliação: soma dos elementos do array
    return sum(solution)

# Define the function to generate neighborhood solutions
def generate_neighborhood(solution):
    neighborhood_solutions = []
    
    # Generate all possible neighbor solutions by changing one number at a time
    for i in range(len(solution)):
        for delta in [-1, 1]:  # Increment or decrement the value
            neighbor_solution = solution.copy()
            neighbor_solution[i] += delta
            neighborhood_solutions.append(neighbor_solution)
    
    return neighborhood_solutions

# Define the Tabu Search function
def tabu_search(initial_solution, tabu_list_size, num_iterations):
    # Initialize the current solution and best solution
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

# Define the initial solution
initial_solution = [random.randint(0, 10) for _ in range(5)]

# Define the tabu list size and number of iterations
tabu_list_size = 50
num_iterations = 1000000

# Execute the Tabu Search
best_solution, best_evaluation = tabu_search(initial_solution, tabu_list_size, num_iterations)

print("Initial Solution:", initial_solution)
print("Best Solution:", best_solution)
print("Best Evaluation:", best_evaluation)