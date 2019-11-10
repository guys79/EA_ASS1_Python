from deap import base
from deap import creator
from deap import tools
from functionDefinitionsAsArray import *
# TODO need to crate new crossover function
# Defining constants
N = 8
pop_size = 1000
mutation_prob = 0.001
crossover_prob = 0.7
max_generation = 10000

def mutate(individual,indpb):
    ind = []
    for line in individual:
        ind.append(tools.mutation.mutFlipBit(line,1/N)[0])
    return ind,

# Defining Fitness kind and Individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox
toolbox = base.Toolbox()

# Attributes
toolbox.register("attr_array", createBoard,N)

# Structure (individual and population)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_array, N)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

#Function definitions
toolbox.register("evaluate", evaluation)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", mutate)
toolbox.register("select", tools.selection.selRoulette)


'''

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.randrange, start=0, stop=NB_QUEENS)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.permutation, n=NB_QUEENS)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalNQueens)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", mutShuffle)
toolbox.register("select", tools.selRoulette)


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
    pop, stats, hof = main()
    print(hof)
'''
def main():
    pop = toolbox.population(n=pop_size)
    # Evaluate the entire population
    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit


    # Extracting all the fitnesses of
    fits = [ind.fitness.values[0] for ind in pop]

    # Variable keeping track of the number of generations
    gen = 0
    #for inf in pop:
    #    printBoard(inf)
     #   print()
    # Begin the evolution
    print(fits)
    print(max(fits) < 0)
    print(gen < max_generation)
    print(max(fits) < 0 and gen < max_generation)
    while max(fits) < N*N and gen < max_generation:
        # A new generation
        gen = gen + 1
        print("-- Generation %i --" % gen)

        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop)) # chosses 0

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))


        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_prob:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < mutation_prob:
                toolbox.mutate(mutant, indpb = mutation_prob)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        # Replace old population with new one
        print(offspring)
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        print(" population size %d" % length)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("Done")
    max2 = -1*N*N
    max_ind = None
    val =0
    length = len(pop)
    print(" population size %d" % length)
    for ind in pop:
        val = evaluation(ind)
        if max2 < val[0]:
            max_ind = ind
            max2 = val[0]
    printBoard(max_ind)
    print(max2)
main()