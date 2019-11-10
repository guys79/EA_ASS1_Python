import random
import numpy
import time

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

NB_QUEENS = 8

def mutShuffle(individual, indpb):

    size = len(individual)
    i = random.randint(0, size - 1)
    swap_indx = random.randint(0, size - 2)
    if swap_indx >= i:
        swap_indx += 1
    individual[i], individual[swap_indx] = \
        individual[swap_indx], individual[i]

    return individual,


def evalNQueens(individual):

    size = len(individual)
    sum_ = 0
    for i in range(size):
        for j in range(i+1, size):
            if individual[i] == individual[j]:
                sum_ += 2
            if (j - i == individual[j] - individual[i]) or (j - i == individual[i] - individual[j]):
                sum_ += 2
    return sum_,




creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalNQueens)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", mutShuffle, indpb=1.0 / NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():

    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Median", numpy.median)
    stats.register("Best", numpy.min)
    stats.register("Worst", numpy.max)

    start_time = time.time()

    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.001, ngen=100, stats=stats, halloffame=hof, verbose=True)

    elapsed_time = time.time() - start_time
    print('%.2f  seconds' % elapsed_time)

    return pop, stats, hof


if __name__ == "__main__":
    pop, stats, hof =main()
    print(hof)