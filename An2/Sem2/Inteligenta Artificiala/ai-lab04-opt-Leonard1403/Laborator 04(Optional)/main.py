from library import *
import matplotlib.pyplot as plt

# Get TSP data
TSP = getTspData('data/berlin52.tsp')
# TSP = getTspData('data/fricker26')
# Display TSP file headers

# displayTspHeaders(TSP)
# displayTspHeaders(matrix_to_edges(readTSPFile('data/berlin.txt')))

# Get Space

# space = np.array(TSP['node_coord_section'])
# print(space)
n, space = read_input_file('data/fricker26.txt')
space = np.array(matrix_to_edges(space))
# print(space)

# Plot nodes
plt.scatter(space[:, 0], space[:, 1], s=15)

# Plot properties
# plt.title('Space {}'.format(TSP['name']))
plt.xlabel('Latitude')
plt.ylabel('Longitude')

# Show plot
plt.show()
plt.close()

# Algorithm Parameters
iterations = 100
colony = 100
alpha = 1
beta = 1
adjust = 1.5
rho = 0.5

# Vars
average = 0

# Run
# min_path, min_distance = mainAco(space, iterations, colony, alpha, beta, adjust, rho)
min_path, min_distance = mainAco(space, iterations, colony, alpha, beta, adjust, rho)
average += min_distance

# Plot path
plt.scatter(space[:, 0], space[:, 1], marker='o', s=15)
plt.plot(space[min_path, 0], space[min_path, 1], c='g', linewidth=0.8, linestyle="--")

# Plot properties
# plt.suptitle('Mininum Path for {}'.format(TSP['name']))
plt.title('Result #{} of {} for a minimum distance of {}'.format(1, 1, int(min_distance)), fontsize=10)
plt.xlabel('Latitude')
plt.ylabel('Longitude')

plt.show()
plt.close()

# Show Average
# print('Min Distance Average for the last {} results is {}'.format(1, average / 1))