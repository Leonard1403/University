import random

# Define parameters
POP_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.01

# Define fitness function
def calculate_fitness(individual, distance_matrix, start_node, end_node):
    total_distance = 0
    current_node = start_node
    for next_node in individual:
        total_distance += distance_matrix[current_node][next_node]
        current_node = next_node
    total_distance += distance_matrix[current_node][end_node]
    return 1 / total_distance

# Define selection function
def selection(population, distance_matrix, start_node, end_node):
    fitness_scores = [calculate_fitness(individual, distance_matrix, start_node, end_node) for individual in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    return random.choices(population, weights=probabilities, k=2)

# Define crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [node for node in parent2 if node not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [node for node in parent1 if node not in parent2[:crossover_point]]
    return child1, child2

# Define mutation function
def mutation(individual):
    if random.random() < MUTATION_RATE:
        index1, index2 = random.sample(range(len(individual)), 2)
        individual[index1], individual[index2] = individual[index2], individual[index1]

# Define main function
def sp_main(distance_matrix, start_node, end_node):
    # Generate initial population
    population = [[i for i in range(len(distance_matrix))] for _ in range(POP_SIZE)]

    # Evolve population
    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(int(POP_SIZE / 2)):
            # Selection
            parent1, parent2 = selection(population, distance_matrix, start_node, end_node)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            mutation(child1)
            mutation(child2)

            # Add new individuals to new population
            new_population.append(child1)
            new_population.append(child2)

        # Replace old population with new population
        population = new_population

    # Select best individual as solution
    best_individual = max(population, key=lambda individual: calculate_fitness(individual, distance_matrix, start_node, end_node))

    # Calculate total distance of best individual
    total_distance = 0
    current_node = start_node
    for next_node in best_individual:
        total_distance += distance_matrix[current_node][next_node]
        current_node = next_node
    total_distance += distance_matrix[current_node][end_node]

    return best_individual, total_distance
