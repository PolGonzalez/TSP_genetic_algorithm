from instance import Instance
from solution import Solution


class GA:
    def __init__(self, instance: Instance, config: dict) -> None:
        self.population = None
        self.instance = instance

        self.best_solution = None
        self.best_cost = 1e9

        self.n_generations = config['n_generations']

    def run(self) -> Solution:
        """Execute the genetic algorithm."""

        feasible_population = self.generate_feasible_population()

        first_generation = self.generate_initial_population(feasible_population)

        self.best_solution = self.simulate_generations(first_generation)
        return self.best_solution

    def generate_feasible_population(self):
        """Generate a feasible population."""

        population = []
        for i in range(0, self.instance.n):
            initial_node = i
            path = [initial_node]
            not_visited = [j for j in range(0, self.instance.n)]
            not_visited.remove(initial_node)
            # we select the closest node to the latest that we have visited until there are no more nodes
            actual = initial_node
            while len(path) < self.instance.n:
                potential = [self.instance.dist[actual][index] for index in not_visited]
                actual = self.instance.dist[actual].index(min(potential))
                path.append(actual)
                not_visited.remove(actual)
            population.append(Solution(self.instance,path))
        return population

    def generate_initial_population(self,population):
        """Generate an initial population."""
        initial_population_2swap = [path.two_swap() for k in range(10) for path in population]
        initial_population_3cycle = [path.three_cycle() for l in range(10) for path in population]
        population = population + initial_population_2swap + initial_population_3cycle
        return population

    def simulate_generations(self,population):
        """Simulate the generations of the genetic algorithm."""
        score = [route.tsp_cost() for route in population]
        best_path_idx, best_score = min(enumerate(score), key=lambda x: x[1])
        best_solution = population[best_path_idx]

        for i in range(0, self.n_generations):
            # create new generation
            population_2swap = [path.two_swap() for k in range(5) for path in population]
            population_3cycle = [path.three_cycle() for k in range(5) for path in population]
            population_22swap = [path.twotwo_swap() for k in range(5) for path in population]
            new_generation = population + population_2swap + population_3cycle + population_22swap

            # check if a better solution has been found
            score = [path.tsp_cost() for path in new_generation]
            if min(score) < best_score:
                best_score, best_path_idx = min((ite, value) for (value, ite) in enumerate(score))
                best_solution = new_generation[best_path_idx]

            # keep best elements
            population = []
            for j in range(0, 50):
                candidate, candidate_path_idx = min((ite, value) for (value, ite) in enumerate(score))
                population.append(new_generation[candidate_path_idx])

        return best_solution

