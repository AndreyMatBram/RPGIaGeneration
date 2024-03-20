from deap import base, creator, tools
import numpy as np
import random
from EvoBattle import evolution

sttsCount= 5
levelCap= 20

plystts = [2,5,10,2,6] # força, magia, defesa, defesa magica, velocidade




def genetic():
    creator.create("FitnessMax", base.Fitness, weights=(1.0,1.0))
    creator.create("Character", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("stts_Float", random.random)
    toolbox.register("character", tools.initRepeat, creator.Character, toolbox.stts_Float, n=sttsCount)

    ind1 = toolbox.character()

    ind1Trunc = [round(stts, 2)*100 for stts in ind1]

    ind1.fitness.values= evolution(ind1Trunc) # (a: int , b: boll )
   

def main():
    genetic()

if __name__ == "__main__":
    main()
