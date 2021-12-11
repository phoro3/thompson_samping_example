from TsAgent import TsAgent
import numpy as np
if __name__ == '__main__':
    agent = TsAgent(3)


    while True:
        print('counts: ', agent.counts)
        print('wins: ', agent.wins)
        print('probas: ', agent.get_arm())
        print('input: ')
        selected = int(input().strip())
        reward = 1 if np.random.random() > 0.5 else 0
        agent.sample(selected, reward)