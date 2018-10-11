import numpy as np
from numpy.random import rand, randint
import gym


def play_game(agent):
    score = 0
    extra_frames = 0
    env = gym.make('CartPole-v0')
    observation, reward, done, info = env.reset()
    observation = [0, 0, 0, 0]
    for i in range(1000):
        env.render()
        score += reward
        observation, reward, done, info = env.step(agent.select_action(observation))
        if done:
            extra_frames += 1
            if extra_frames == 5:
                env.close()
                break
    return score


class Random_Walk_Agent(object):
    def __init__(self, w):
        self.w = w
        self.best_score = -1

    def select_action(self, obs):
        obs = np.array(obs)
        s = np.sum(self.w * obs)
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


def cycle(agent, N=10):
    s = 0    
    for _ in range(N):
        s += play_game(agent)
    print(s / N)
    return s / N


def random_walk(agent):
    # random walk
    w0 = agent.get_weights()
    i_rand = randint(0, 3)
    wnew = w0
    new_weight = (rand() * 2) - 1
    print(new_weight, i_rand)
    wnew[i_rand] += new_weight
    print(wnew)
    agent.update_weights(wnew)
    s = cycle(agent, 3)
    if s < agent.get_score():
        agent.update_weights(w0)
        print('rejected')
    else:
        print('kept')


def run():
    # create agent with initial weights
    w_i = np.array([0, 0, 0, 0])
    walker = Random_Walk_Agent(w_i)

    # find average score
    s = cycle(walker, 3)
    walker.update_score(s)

    for _ in range(10):
        random_walk(walker)

    


run()





