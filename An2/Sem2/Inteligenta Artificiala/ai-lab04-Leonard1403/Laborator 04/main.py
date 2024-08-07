import numpy as np

from ga_sp import sp_main
from ga_tsp import genetic_algorithm
from ga_tsp_v2 import TSPGeneticAlgorithm

def read_input():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split(",")))
        matrix.append(row)
    a, b = map(int, input().split())
    return n, matrix, a, b

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

import math


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


def main():
    # n, distances = read_input_file("data/easy_01_tsp.txt")
    # n, distances, start_node, end_node = read_input_file("data/fricker26.txt")
    # n, distances = read_input_file("data/fricker26.txt")
    distances = readTSPFile("data/berlin.txt")

    print(distances)
    # print(start_node)
    # print(end_node)

    solution = genetic_algorithm(distances,500,100,100,100)
    # solution = TSPGeneticAlgorithm(distances, 500, 100, 100, 100)
    best_route = solution.solve()
    print(best_route)

    # solution2, total_distance2 = sp_main(distances,start_node-1,end_node-1)

    # i = 0
    # total_distance = 0
    # n = len(solution)
    # for el in solution:
    #     solution[i] = el + 1
    #     i = i + 1
    #     if i<n:
    #         total_distance = total_distance + distances[solution[i-1]-1][solution[i]]
    #         print(solution[i-1]-1,solution[i],distances[solution[i-1]-1][solution[i]])
    # total_distance = total_distance + distances[solution[n-1]-1][solution[0]-1]
    # print("Solutie: ",solution)
    # print(total_distance)
    # print("Solutie2: ", solution2)
    # print(total_distance2)
main()