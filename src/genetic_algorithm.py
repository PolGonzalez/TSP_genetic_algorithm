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

        self.generate_feasible_population()

        self.generate_initial_population()

        self.simulate_generations()

        self.best_solution = Solution(self.instance, list(range(0, self.instance.n)))
        return self.best_solution

    def generate_feasible_population(self) -> None:
        """Generate a feasible population."""
        pass

    def generate_initial_population(self) -> None:
        """Generate an initial population."""
        pass

    def simulate_generations(self) -> None:
        """Simulate the generations of the genetic algorithm."""
        pass
