import numpy as np
from numpy.random import rand, randint
import os
import sys
import gym


def play_game(agent):
    score = 0
    save_stdout = sys.stdout
    sys.stdout = open('trash', 'w')
    env = gym.make('CartPole-v0')
    sys.stdout = save_stdout
    os.remove('trash')
    observation, reward, done, info = env.reset()
    observation = [0, 0, 0, 0]
    for i in range(1000):
        env.render()
        score += reward
        observation, reward, done, info = env.step(agent.select_action(observation))
        if done:
            env.close()
            break
    return score


class Random_Walk_Agent(object):
    def __init__(self, w):
        self.w = w
        self.best_score = -1

    def select_action(self, obs):
        obs = np.array(obs)
        obs_array = np.zeros(len(obs)*2)
        obs_array[:len(obs)] = obs
        obs_array[len(obs):] = obs ** 2
        s = np.sum(self.w * obs_array)
        if s >= 0:
            action = 0
        else:
            action = 1
        return action

    def update_score(self, s):
        self.best_score = s

    def get_weights(self):
        return self.w

    def update_weights(self, w):
        self.w = w

    def get_score(self):
        return self.best_score


def cycle(agent, N=5):
    s = 0
    for _ in range(N):
        s += play_game(agent)
    print(s / N)
    return s / N


def random_walk(agent):
    # random walk
    w0 = agent.get_weights()
    i_rand = randint(0, len(w0))
    wnew = w0
    step = 0.1
    new_weight = (rand() * step) - (step * 0.5)
    wnew[i_rand] += new_weight
    agent.update_weights(wnew)
    s = cycle(agent)
    if s < agent.get_score():
        agent.update_weights(w0)
    else:
        agent.update_score(s)
        print(wnew)
    return


def learn(w_i):
    # create agent with initial weights
    walker = Random_Walk_Agent(w_i)

    # find average score
    s = cycle(walker)
    walker.update_score(s)

    for _ in range(10):
        random_walk(walker)

    # return final weights
    return walker.get_weights()


if __name__ == '__main__':
    try:
        w_i = np.load('weights.npy')
        print('Loaded Weights')
    except:
        w_i = np.zeros(8)
        print('New Weights')
    w_f = learn(w_i)
    np.save('weights.npy', w_f)
