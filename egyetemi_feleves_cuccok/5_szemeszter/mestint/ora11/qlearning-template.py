class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate
        
        # TODO: Generate an n_states*n_actions matrix
        self.q_table = None
    
    def act(self, state, epsilon):
        # TODO: Generate a random number on the [0, 1) interval
        random_int = None
        
        # TODO: We exploit with (1-epsilon) probability
        if random_int > epsilon:
            action = None
        # TODO: We explore with epsilon probability
        else:
            action = None
        
        return action
    
    def learn(self, state, action, reward, new_state, gamma):
        # TODO
        old_value = None
        new_estimate = None
        
        # Update the approximation of the Q-value
        self.q_table[state][action] = old_value + self.learning_rate * (new_estimate- old_value)   