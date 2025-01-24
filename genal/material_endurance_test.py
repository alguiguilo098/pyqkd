import math
import genetic_algorithm
import selection_operators
import crossover_operators
import pygad
import numpy as np


def endurance(x, y, z, u, v, w):
    """Function to be optimised"""
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


def fitness_function_pygad(genetic_algorithm_instance, chromosome, chromosome_idx):
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    u = chromosome[3]
    v = chromosome[4]
    w = chromosome[5]

    fitness_value = endurance(x=x, y=y, z=z, u=u, w=w, v=v)

    return fitness_value


def fitness_function(chromosome):
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    u = chromosome[3]
    v = chromosome[4]
    w = chromosome[5]

    fitness_value = endurance(x=x, y=y, z=z, u=u, w=w, v=v)

    return fitness_value


if __name__ == '__main__':
    """Firstly, solving problem with pygad:"""
    ga_instance = pygad.GA(
        gene_space=np.linspace(start=0, stop=1, num=100000),
        num_generations=70,
        num_parents_mating=9,
        fitness_func=fitness_function_pygad,
        sol_per_pop=18,
        num_genes=6,
        parent_selection_type='tournament',
        mutation_type='random',
        mutation_probability=float(1 / 6),
        stop_criteria=['reach_2.83', 'saturate_15']
    )

    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    generations_number = ga_instance.best_solution_generation

    print(f"Best solution: {solution}")
    print(f"Fitness value of the best solution: {solution_fitness}")
    print(f"It took {generations_number} generations to find an optimal solution.")

    #  ga_instance.plot_fitness()
