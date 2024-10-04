
import numpy as np
import pygad
from EvoBattle import evolution

plystts = [12,32,25,21,14]
levelCap = sum(plystts[:5]) 

# Função de fitness
def fitness_func(instance ,solution, solution_idx):
    # Conversão da solução para uma lista
    iastts = solution[:5]
    # Chamada da função de evolução
    a = evolution(iastts, plystts, levelCap)
    return a

# Definição do problema
num_genes = 5
sol_per_pop = 20
num_parents_mating = 5
mutation_probability = 0.1
initial_population = np.random.randint(1, int(levelCap/5)*2, (sol_per_pop, num_genes))

# Criação da instância do PyGAD
ga_instance = pygad.GA( num_generations=1000,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness_func,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        mutation_probability=mutation_probability,
                        initial_population=initial_population,
                        )

# Execução do algoritmo genético
ga_instance.run()

# Melhor solução encontrada
melhor_solucao, melhor_fitness, melhor_validade = ga_instance.best_solution()

print(f"Melhor solução: {melhor_solucao}")
print(f"Vida Restante: {melhor_fitness}")