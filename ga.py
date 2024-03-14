# genetik_algoritma.py
from geopy.distance import geodesic
import random
import copy

class GeneticAlgorithm:
    def __init__(self, population_size, iteration_count, crossover_rate, mutation_rate, points, distance_matrix):
        self.population_size = population_size
        self.iteration_count = iteration_count
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.points = points
        self.distance_matrix = distance_matrix
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            path = list(range(len(self.points)))
            random.shuffle(path)
            population.append(path)
        return population

    def calculate_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i]][route[i + 1]]
        distance += self.distance_matrix[route[-1]][route[0]]
        return distance

    def calculate_fitness(self, individual):
        return 1 / (self.calculate_distance(individual) + 1e-10)

    def crossover(self, parent1, parent2):
        point1 = random.randint(0, len(parent1) - 1)
        point2 = random.randint(point1, len(parent1) - 1)
        child = [None] * len(parent1)
        child[point1:point2] = parent1[point1:point2]
        for i in range(len(parent2)):
            if parent2[i] not in child:
                for j in range(len(child)):
                    if child[j] is None:
                        child[j] = parent2[i]
                        break
        return child

    def mutate(self, individual):
        point1 = random.randint(0, len(individual) - 1)
        point2 = random.randint(0, len(individual) - 1)
        individual[point1], individual[point2] = individual[point2], individual[point1]
        return individual

    def create_new_individual(self):
        fitness_values = [self.calculate_fitness(individual) for individual in self.population]
        new_individuals = []

        for _ in range(self.population_size):
            parent1, parent2 = random.choices(self.population, weights=fitness_values, k=2)
            if random.random() < self.crossover_rate:
                child = self.crossover(parent1, parent2)
            else:
                child = copy.deepcopy(random.choice([parent1, parent2]))
            if random.random() < self.mutation_rate:
                child = self.mutate(child)
            new_individuals.append(child)

        self.population = new_individuals

    def get_best_route(self):
        fitness_values = [self.calculate_fitness(individual) for individual in self.population]
        best_index = fitness_values.index(max(fitness_values))
        return self.population[best_index], 1 / fitness_values[best_index]

    def optimize(self):
        for _ in range(self.iteration_count):
            self.create_new_individual()

        best_route, best_fitness = self.get_best_route()
        return best_route, best_fitness
