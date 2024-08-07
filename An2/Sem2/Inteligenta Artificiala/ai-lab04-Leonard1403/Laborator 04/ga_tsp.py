import random

# function to calculate fitness of a chromosome
def fitness(chromosome, distances):
    total_distance = 0
    for i in range(len(chromosome)-1):
        total_distance += distances[chromosome[i]][chromosome[i+1]]
    total_distance += distances[chromosome[len(chromosome)-1]][chromosome[0]]
    return 1/total_distance

# function to generate an initial population of chromosomes
def generate_population(size, num_nodes):
    population = []
    for i in range(size):
        chromosome = list(range(num_nodes))
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

# function to perform selection of fittest chromosomes
def selection(population, distances, elite_size):
    fitness_scores = [(chromosome, fitness(chromosome, distances)) for chromosome in population]
    # print("Fitnes: ", fitness_scores)
    fitness_scores.sort(key=lambda x: x[1], reverse=True)
    selected = [chromosome for chromosome, score in fitness_scores[:elite_size]]
    return selected

# function to perform crossover of parent chromosomes
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    # print("parent: ", parent1)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    # print(start, end)
    # print(start,end)
    child[start:end+1] = parent1[start:end+1]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# function to perform mutation of a chromosome
def mutation(chromosome):
    idx1, idx2 = random.sample(range(len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# function to run the genetic algorithm
def genetic_algorithm(distances, population_size=100, elite_size=20, mutation_rate=0.01, generations=100):
    # print(len(distances))
    population = generate_population(population_size, len(distances))
    total_distance = 0
    for i in range(generations):
        selected = selection(population, distances, elite_size)
        offspring = []
        for j in range(len(population) - elite_size):
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutation(child)
            offspring.append(child)
        population = selected + offspring
        fittest = max(population, key=lambda x: fitness(x, distances))
        current_distance = 1/fitness(fittest, distances)
        if current_distance > total_distance:
            total_distance = current_distance
            best_solution = fittest
        print("Generation", i, "- Best solution:", fittest, "- Distance:", current_distance, "- Total Distance:", total_distance)
    print("Final solution:", best_solution)
    print("Fitness:", total_distance)
    return best_solution

