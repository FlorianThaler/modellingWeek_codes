from matplotlib import pyplot as plt
import numpy as np

from itertools import product

from myStrategicGames import MyAnnoyingNeighbourGame

def strategy_cooperative(history1, history2):
    return 'q'

def strategy_nonCooperative(history1, history2):
    return 'l'

def simulateGame(S1, s2, numDraws = 1000):

    history_1 = []
    history_2 = []

    cumPayoff_1 = 0.0
    cumPayoff_2 = 0.0

    for i in range(0, numDraws):

        a1 = s1(history_1, history_2)
        a2 = s2(history_1, history_2)

        history_1.append(a1)
        history_2.append(a2)

        payoff = game.getPayoff(a1, a2)

        cumPayoff_1 += payoff[0]
        cumPayoff_2 += payoff[1]
    
    return cumPayoff_1, cumPayoff_2

def evolutionaryCompetition(strategyDict):
    numPopulationsPerStrategy = 100
    numGenerations = 20

    strategyKeys = strategyDict.keys()

    numStrategies = len(strategyDict)
    totNumPopulations = numStrategies * numPopulationsPerStrategy
    popRates = (1 / numStrategies) * np.ones(numStrategies)



    for i in range(0, numGenerations):
        strategyPool = []

        # ### create population according to rates
        for j in range(0, len(popRates) - 1):
            strategyPool += [strategyDict[strategyKeys[j]] for l in range(0, int(popRates[j] * totNumPopulations))]

        strategyPool += [strategyDict[strategyKeys[-1]] for l in range(len(strategyPool), totNumPopulations)]

        # ### evaluate strategies by means of tournament

        # ### update population rates according to the result of the tournament



    
    for key in strategyDict.keys():
        for i in range(0, numPopulationsPerStrategy):
            strategyPool.append((key, strategyDict[key]))

    

def tournament(strategyDict):
    """
        this function is used to compare strategies with each other. for this purpose each strategy meets other
        strategy (including itself) over a predefinednumber of draws. the cumulative payoffs are used to evaluate
        the strategies.

    Args:
        strategyDict (dictionary): dictionary containing strategies, which are represented by means of functions

    Returns:
        dictionary: dict representing the sorted (by cumulative payoffs) scoreboard of the tournament
    """

    scoreboard = {}
    for key in strategyDict.keys():
        scoreboard[key] = 0.0

    tournamentTable = [elem for elem in product(strategyDict.keys(), strategyDict.keys())]

    numDraws = 1000

    for elem in tournamentTable:

        cumPayoff_1, cumPayoff_2 = simulateGame(strategyDict[elem[0]], strategyDict[elem[1]], numDraws)
        scoreboard[elem[0]] += cumPayoff_1
        scoreboard[elem[1]] += cumPayoff_2

    scoreboard_sorted = sorted(scoreboard.items(), key = lambda elem: elem[1], reverse = True)

    return scoreboard_sorted

if __name__ == '__main__':

    game = MyAnnoyingNeighbourGame()

    strategyDict = {}
    strategyDict['coop'] = strategy_cooperative
    strategyDict['nonCoop'] = strategy_nonCooperative


    numReps = 100

    
    payoffList_1 = []
    payoffList_2 = []

    for i in range(1, numReps):

        
        payoffList_1.append(payoff[0])
        payoffList_2.append(payoff[1])


    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(np.arange(0, len(payoffList_1)), payoffList_1)

    plt.show()
    
