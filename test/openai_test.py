import time

import gym
env = gym.make('MsPacman-ram-v0')
env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    print(2)
    env.step(2) # take a random action
    time.sleep(0.1)