# Flappy-Bird-using-RL
The code in this repository is used to train agents to play FlappyBird using techniques from reinforcement learning. Q-Learning and SARSA are implemented.

## Names:
Roja Immanni

## Research Question:
We applied different Reinforcement Learning algorithms train an agent to play FlappyBird game forever?

## Reinforcement Learning Framework
For this game, We can frame the RL problem in the following way
- Environment: Flappybird's game space
- Agent: Agent is the flappybird who decides either to do nothing or jump
- States: Flappybird's vertical distance from the ground, horizontal distance from the next pipe and its speed
- Actions: Actions would be either to do nothing or jump
- Rewards: positive reward(+1) if the bird is still alive and negative reward(-1000) if it hits and dies

## Code files
Code for environment can be found at https://github.com/RojaImmanni/Flappy-Bird-using-RL/blob/master/environment.py

Code for random agent can be found at https://github.com/RojaImmanni/Flappy-Bird-using-RL/blob/master/RandomAgent.py

Code for a trainable agent can be found at https://github.com/RojaImmanni/Flappy-Bird-using-RL/blob/master/TrainableAgent.py





Resources:
1. https://arxiv.org/pdf/2003.09579v1.pdf
