import numpy as np

def read_input_file(filename):
    with open(filename, 'r') as f:
        n = int(f.readline())
        matrix = []
        for i in range(n):
            row = list(map(int, f.readline().strip().split(",")))
            matrix.append(row)
        # a = int(f.readline())
        # b = int(f.readline())
    # return n, matrix, a, b
    return n, matrix

def readTSPFile(filePath):
    # read a file in TSPLIB format
    # NAME: berlin52
    # TYPE: TSP
    # COMMENT: 52 locations in Berlin (Groetschel)
    # DIMENSION: 52
    # EDGE_WEIGHT_TYPE: EUC_2D
    # NODE_COORD_SECTION

    # read the file
    with open(filePath, 'r') as f:
        lines = f.readlines()

    # get the dimension
    for line in lines:
        if line.startswith('DIMENSION'):
            dim = int(line.split(':')[1])
            break

    # get the coordinates
    coords = []
    for i in range(len(lines)):
        if lines[i].startswith('NODE_COORD_SECTION'):
            for j in range(i + 1, i + dim + 1):
                coords.append(lines[j].split()[1:3])
            break

    # compute the distance matrix
    dist = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            dist[i][j] = np.sqrt(
                (float(coords[i][0]) - float(coords[j][0])) ** 2 + (float(coords[i][1]) - float(coords[j][1])) ** 2)

    # transform into network
    network = []
    for i in range(dim):
        numbers = []
        for j in range(dim):
            numbers.append(dist[i][j])
        network.append(numbers)
    return network

def matrix_to_edges(matrix):
    """
    Transforms a matrix with distances into a list of edges for a graph.

    Args:
    - matrix (list of lists): The input matrix representing distances between nodes.

    Returns:
    - list of tuples: A list of edges for the graph.
    """
    edges = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != 0:
                edges.append([i, j])

    return edges


def getTspData(tsp):
    # Open input file
    infile = open(tsp, 'r')

    name = infile.readline().strip().split()[1]
    type = infile.readline().strip().split()[1]
    comment = infile.readline().strip().split()[1]
    dimension = infile.readline().strip().split()[1]
    edge_weight_type = infile.readline().strip().split()[1]
    node_coord_section = []
    infile.readline()

    # Read node coord section and store its x, y coordinates
    for i in range(0, int(dimension)):
        x, y = infile.readline().strip().split()[1:]
        node_coord_section.append([float(x), float(y)])

    # Close input file
    infile.close()

    # File as dictionary
    return {
        'name': name,
        'type': type,
        'comment': comment,
        'dimension': dimension,
        'edge_weight_type': edge_weight_type,
        'node_coord_section': node_coord_section
    }

def displayTspHeaders(dict):
    print('\nName: ', dict['name'])
    print('Type: ', dict['type'])
    print('Comment: ', dict['comment'])
    print('Dimension: ', dict['dimension'])
    print('Edge Weight Type: ', dict['edge_weight_type'], '\n')

# This is the main function that implements the ACO algorithm for the TSP.
# It takes as input the distance matrix (space), number of iterations (iterations),
# number of ants in the colony (colony), and various algorithm parameters
# such as alpha, beta, del_tau, and rho. It returns the best found tour (path) and its corresponding distance (cost).

def mainAco(space, iterations = 80, colony = 50, alpha = 1.0, beta = 1.0, adjust = 1.0, removePheromon = 0.5):
    # [1] Find inverted distances for all nodes
    inv_distances = inverseDistances(space)

    # Add beta algorithm parameter to inverted distances
    inv_distances = inv_distances ** beta

    # Empty pheromones trail
    pheromones = np.zeros((space.shape[0], space.shape[0]))

    # Empty minimum distance and path
    min_distance = None
    min_path = None

    # [2] For the number of iterations
    for i in range(iterations):
        # Initial random positions
        positions = initializeAnts(space, colony)

        # Complete a path
        paths = moveAnts(space, positions, inv_distances, pheromones, alpha, beta, adjust)
        last_distance = 0

        # Evaporate pheromones
        pheromones *= (1 - removePheromon)

        # [3] For each path
        for path in paths:
            # Empty distance
            distance = 0

            # For each node from second to last
            for node in range(1, path.shape[0]):
                # Calculate distance to the last node
                distance += np.sqrt(((space[int(path[node])] - space[int(path[node - 1])]) ** 2).sum())
                # last_distance = np.sqrt(((space[int(path[node])] - space[int(path[node - 1])]) ** 2).sum())

            # Update minimun distance and path if less nor non existent
            if not min_distance or distance < min_distance:
                min_distance = distance
                min_path = path

        # Copy and append first node to end of minimum path to form closed path
        min_path = np.append(min_path, min_path[0])

        # Return tuple
        return (min_path, min_distance)

def inverseDistances(space):
    # Empty multidimensional array (matriz) to distances
    distances = np.zeros((space.shape[0], space.shape[0]))

    # Calculate distance to all nodes to all nodes
    for index, point in enumerate(space):
        distances[index] = np.sqrt(((space - point) ** 2).sum(axis = 1))

    # Floating-point error handling - Setted to known state
    with np.errstate(all = 'ignore'):
        # Invert the distances
        inv_distances = 1 / distances

    # Replace infinity by zero to prevent zero division error
    inv_distances[inv_distances == np.inf] = 0

    # Eta algorithm result, inverted distances
    return inv_distances

def initializeAnts(space, colony):
    # Indexes of initial positions of ants
    return np.random.randint(space.shape[0], size = colony)

def moveAnts(space, positions, inv_distances, pheromones, alpha, beta, adjust):
    # Empty multidimensional array (matriz) to paths
    paths = np.zeros((space.shape[0], positions.shape[0]), dtype = int) - 1

    # Initial position at node zero
    paths[0] = positions

    # For nodes after start to end
    for node in range(1, space.shape[0]):
        # For each ant
        for ant in range(positions.shape[0]):
            # Probability to travel the nodes
            next_location_probability = (inv_distances[positions[ant]] ** alpha + pheromones[positions[ant]] ** beta /
                                            inv_distances[positions[ant]].sum() ** alpha + pheromones[positions[ant]].sum() ** beta)

            # Index to maximum probability node
            next_position = np.argwhere(next_location_probability == np.amax(next_location_probability))[0][0]

            # Check if node has already been visited
            while next_position in paths[:, ant]:
                # Replace the probability of visited to zero
                next_location_probability[next_position] = 0.0

                # Find the maximum probability node
                next_position = np.argwhere(next_location_probability == np.amax(next_location_probability))[0][0]

            # Add node to path
            paths[node, ant] = next_position

            # Update pheromones (releasing pheromones)
            pheromones[node, next_position] = pheromones[node, next_position] + adjust

    # Paths taken by the ants
    return np.swapaxes(paths, 0, 1)