import numpy as np
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


class Cart_Pole_Agent(object):
    def __init__(self, w):
        self.w = w

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


class Node(object):
    def __init__(self, w):
        self.w = w
        self.h = None


def expand(node):
    step = 0.05
    expanded = []
    for i, weight in enumerate(node.w):
        w_new0 = node.w.copy()
        w_new0[i] = weight + step
        expanded.append(Node(w_new0))
        w_new1 = node.w.copy()
        w_new1[i] = weight - step
        expanded.append(Node(w_new1))
    return expanded


def h(node):
    N = 5
    score = 0
    for _ in range(5):
        agent = Cart_Pole_Agent(node.w)
        score += play_game(agent)
    return score / N


def beam_search(start_node, closed_list=[], open_list=[]):
    # remove start_node from queue
    closed_list.append(start_node)

    # expand start node
    expanded = expand(start_node)

    # if node isn't in the closed list, add it to the open list
    for n_e in expanded:
        in_closed = False
        for n_c in closed_list:
            if np.all(n_c.w == n_e.w):
                in_closed = True
        if not in_closed:
            open_list.append(n_e)

    # if the h(n) hasn't been calculated, do so
    for node in open_list:
        if node.h is None:
            node.h = h(node)

    # sort open list
    open_list = sorted(open_list, key=lambda x: x.h)

    # remove best value
    best = open_list.pop()

    # print run status
    s = 'Current Status\n'
    s += 'Closed: {}\n'.format(len(closed_list))
    s += 'Open: {}\n'.format(len(open_list))
    s += 'Current Score: {}\n'.format(best.h)
    s += '\n'
    print(s)

    # return successful node, failure or recurse
    if best.h > 195:
        return best
    elif not len(open_list):
        return False
    else:
        return beam_search(best, closed_list, open_list)


if __name__ == '__main__':
    start_weights = np.zeros(8)
    start_node = Node(start_weights)
    goal_node = beam_search(start_node)
    print('Goal Node: ', goal_node.w)
