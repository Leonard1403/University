import numpy as np

# functia pentru initializarea matricei de feromoni
def init_pheromone_matrix(num_nodes, initial_pheromone):
    return np.ones((num_nodes, num_nodes)) * initial_pheromone

# functia pentru generarea formei posibile de solutie
def generate_solution(num_nodes):
    return np.random.permutation(num_nodes)

# functia pentru calcularea costului unui traseu
def calculate_cost(solution, distances):
    cost = 0
    num_nodes = len(solution)
    for i in range(num_nodes):
        cost += distances[solution[i], solution[(i+1)%num_nodes]]
    return cost

# functia pentru actualizarea matricei de feromoni
def update_pheromone_matrix(pheromone_matrix, solutions, distances, decay_factor, evaporation_rate, quality_measure):
    # actualizare globala a feromonilor
    pheromone_matrix *= (1 - evaporation_rate)
    num_solutions = len(solutions)
    for i in range(num_solutions):
        cost = calculate_cost(solutions[i], distances)
        for j in range(len(solutions[i])):
            pheromone_matrix[solutions[i][j], solutions[i][(j+1)%num_nodes]] += quality_measure(cost, distances[solutions[i][j], solutions[i][(j+1)%num_nodes]])
    return pheromone_matrix

# functia pentru alegerea urmatorului nod
def select_next_node(pheromone_matrix, current_node, unvisited_nodes, alpha, beta):
    pheromone_sum = np.power(pheromone_matrix[current_node, unvisited_nodes], alpha) * np.power(1.0 / distances[current_node, unvisited_nodes], beta)
    probabilities = pheromone_sum / np.sum(pheromone_sum)
    next_node = np.random.choice(unvisited_nodes, p=probabilities)
    return next_node

# functia principala ACO
def aco_tsp(distances, num_ants, num_iterations, initial_pheromone, decay_factor, evaporation_rate, alpha, beta, quality_measure):
    num_nodes = len(distances)
    pheromone_matrix = init_pheromone_matrix(num_nodes, initial_pheromone)
    best_solution = None
    best_cost = np.inf
    for i in range(num_iterations):
        solutions = []
        for j in range(num_ants):
            # generare solutie
            unvisited_nodes = set(range(num_nodes))
            current_node = np.random.choice(range(num_nodes))
            solution = [current_node]
            unvisited_nodes.remove(current_node)
            for k in range(num_nodes-1):
                next_node = select_next_node(pheromone_matrix, current_node, list(unvisited_nodes), alpha, beta)
                solution.append(next_node)
                unvisited_nodes.remove(next_node)
                current_node = next_node
            solutions.append(solution)
            # actualizare solutie globala optima
            cost = calculate_cost(solution, distances)
            if cost < best_cost:
                best_solution = solution
                best_cost = cost
        # actualizare matrice de feromoni
        pheromone_matrix = update_pheromone_matrix(pheromone_matrix, solutions, distances, decay_factor, evaporation_rate, quality_measure)
    return best_solution
