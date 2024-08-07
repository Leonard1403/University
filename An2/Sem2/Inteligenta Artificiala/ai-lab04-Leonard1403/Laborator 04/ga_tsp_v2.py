import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


class TSPGeneticAlgorithm:
    def __init__(self, city_distances, population_size, elite_size, mutation_rate, generations):
        self.city_distances = city_distances
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.generations = generations

    def calculate_distance(self, route):
        distance = 0
        for i in range(1, len(route)):
            city1 = route[i]
            city2 = route[i - 1]
            distance += self.city_distances[city1][city2]
        return distance

    def create_route(self):
        route = list(range(len(self.city_locations)))
        random.shuffle(route)
        return route

    def initial_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.create_route())
        return population

    def rank_routes(self, population):
        distances = {}
        for i, route in enumerate(population):
            distances[i] = self.calculate_distance(route)
        sorted_distances = sorted(distances.items(), key=operator.itemgetter(1))
        sorted_routes = [population[item[0]] for item in sorted_distances]
        return sorted_routes

    def selection(self, population):
        ranked_population = self.rank_routes(population)
        elite = ranked_population[:self.elite_size]
        selection_pool = ranked_population[self.elite_size:]
        for i in range(len(selection_pool)):
            index1 = random.randint(0, len(selection_pool)-1)
            index2 = random.randint(0, len(selection_pool)-1)
            selected_route = self.crossover(selection_pool[index1], selection_pool[index2])
            selection_pool[i] = selected_route
        return elite + selection_pool

    def crossover(self, route1, route2):
        gene1 = int(random.random() * len(route1))
        gene2 = int(random.random() * len(route1))
        start_gene = min(gene1, gene2)
        end_gene = max(gene1, gene2)
        new_route = [-1] * len(route1)
        for i in range(start_gene, end_gene):
            new_route[i] = route1[i]
        for i in range(len(route2)):
            if route2[i] not in new_route:
                for j in range(len(new_route)):
                    if new_route[j] == -1:
                        new_route[j] = route2[i]
                        break
        return new_route

    def mutation(self, route):
        for i in range(len(route)):
            if random.random() < self.mutation_rate:
                j = int(random.random() * len(route))
                route[i], route[j] = route[j], route[i]
        return route

    def evolve_population(self, population):
        return self.mutation(self.selection(population))

    def solve(self):
        population = self.initial_population()
        best_distance = self.calculate_distance(population[0])
        best_route = population[0]
        distances = [best_distance]

        for i in range(self.generations):
            population = self.evolve_population(population)
            current_distance = self.calculate_distance(population[0])
            if current_distance < best_distance:
                best_distance = current_distance
                best_route = population[0]
            distances.append(best_distance)

        print("Best distance: ", best_distance)