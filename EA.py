from deap import base
from deap import creator
from deap import tools
from functionDefinitionsAsArray import *

# Defining constants
N = 8
pop_size = 100
mutation_prob = 0.001
crossover_prob = 0.7
max_generation = 100


# Defining Fitness kind and Individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox
toolbox = base.Toolbox()

# Attributes
toolbox.register("attr_array", createBoard,N)

# Structure (individual and population)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_array, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
