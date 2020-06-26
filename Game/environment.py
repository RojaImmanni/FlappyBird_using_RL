from ple.games.flappybird import FlappyBird
from ple import PLE
from gym import spaces

import numpy as np
import pandas as pd
import gym
import random
from collections import defaultdict
import os
import sys
sys.path.append("/path/to/PyGame-Learning-Environment")
# to disable the python game window popup
os.environ["SDL_VIDEODRIVER"] = "dummy"


class Game(gym.Env):
    def __init__(self, display_screen=False, force_fps=True):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        game = FlappyBird()  # define and initiate the environment
        self.env = PLE(game, fps=30, display_screen=display_screen,
                       force_fps=force_fps)
        self.env.init()
        # list of actions in the environment
        self.actions = self.env.getActionSet()
        # length of actions
        self.action_space = spaces.Discrete(len(self.actions))

    def step(self, action):
        """Take the action chosen and update the reward"""
        reward = self.env.act(self.actions[action])
        state = self.getGameState()
        terminal = self.env.game_over()

        # If the bird is stuck, the game is over and a reward of -1000
        # if it continues, +1
        if terminal:
            reward = -1000
        else:
            reward = 1

        return state, reward, terminal, {}

    def getGameState(self):
        '''
        PLEenv return gamestate as a dictionary. Returns a modified form
        of the gamestate only with the required information to define the state
        '''
        state = self.env.getGameState()
        h_dist = state['next_pipe_dist_to_player']
        v_dist = state['next_pipe_bottom_y'] - state['player_y']
        vel = state['player_vel']

        return ' '.join([str(vel), str(h_dist), str(v_dist)])

    def reset(self):
        """Resets the game to start a new game"""
        self.env.reset_game()
        state = self.env.getGameState()
        return state

    def seed(self, seed):
        rng = np.random.RandomState(seed)
        self.env.rng = rng
        self.env.game.rng = self.env.rng

        self.env.init()
