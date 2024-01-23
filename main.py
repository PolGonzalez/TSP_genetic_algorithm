from genetic_algorithm import GA
from instance import Instance
import yaml
from pyinstrument import Profiler

if __name__ == '__main__':

    profiler = Profiler()
    profiler.start()

    # Read config.yaml
    with open("config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    instance = Instance()

    ga_config = config['ga_config']
    ga = GA(instance, ga_config)

    best_solution = ga.run()
    #best_solution.save()
    print(best_solution)
    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))
