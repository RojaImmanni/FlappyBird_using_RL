class SARSA_Agent():
    def __init__(self, actions, epsilon=0.0, discount=1, alpha=0.9):
        self.actions = actions
        self.game = Game()
        self.Q = defaultdict(float)
        self.initial_epsilon = epsilon
        self.discount = discount
        self.alpha = alpha

    def select_action(self, state):
        """Exploration and exploitation"""
        if random.random() < self.epsilon:
            return np.random.choice(self.game.action_space.n)

        qValues = [self.Q.get((state, action), 0) for action in self.actions]

        if qValues[0] < qValues[1]:
            return 1
        elif qValues[0] > qValues[1]:
            return 0
        else:
            return np.random.choice(self.game.action_space.n)

    def update_Q(self, state, action, reward, next_state, next_action):
        """Update the Q value based on SARSA on-policy"""

        self.Q[(state, action)] = (1 - self.alpha) * \
            self.Q.get((state, action), 0) + self.alpha * \
            (reward + self.discount * self.Q.get((next_state, next_action), 0))

    def train(self, n_iters, n_iters_eval):
        """ Train the agent"""

        done = False
        max_score = 0
        max_reward = 0
        self.game.seed(random.randint(0, 100))
        test_scores = []

        for i in range(n_iters):

            self.epsilon = self.initial_epsilon
            score = 0
            total_reward = 0
            ob = self.game.reset()
            list_sarsa = []
            state = self.game.getGameState()
            # find the next best action based on e-greedy approach
            action = self.select_action(state)

            while True:
                # take the action and find the next step
                next_state, reward, done, _ = self.game.step(action)
                next_action = self.select_action(next_state)
                list_sarsa.append((state, action, reward, next_state,
                                   next_action))
                state = next_state
                action = next_action

                total_reward += reward
                if reward >= 1:
                    score += 1
                if done:
                    break

            if score > max_score:
                max_score = score
            if total_reward > max_reward:
                max_reward = total_reward

            for (state, action, reward, next_state, next_action) in list_sarsa:
                self.update_Q(state, action, reward, next_state, next_action)

            if i % 250 == 0:
                print("Iter: ", i)

            # Evaluate the model after every 500 iterations
            if (i + 1) % 500 == 0:
                max_score = self.evaluate(n_iter=n_iters_eval)
                test_scores.append(max_score)

        df = pd.DataFrame(test_scores, columns=['scores'])
        df.to_csv("sarsa.csv")
        self.game.close()

    def evaluate(self, n_iter):
        """evaluates the agent"""

        self.epsilon = 0
        self.game.seed(0)

        done = False
        max_score = 0
        max_reward = 0
        output = defaultdict(int)

        for i in range(n_iter):
            score = 0
            total_reward = 0
            ob = self.game.reset()
            state = self.game.getGameState()

            while True:
                action = self.select_action(state)
                state, reward, done, _ = self.game.step(action)
                total_reward += reward
                if reward >= 1:
                    score += 1
                if done:
                    break

            output[score] += 1
            if score > max_score:
                max_score = score
            if total_reward > max_reward:
                max_reward = total_reward

        self.game.close()
        print("Max Score on Evaluation: ", max_score)

        return max_score
