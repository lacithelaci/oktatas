import pygame
import numpy as np
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Signs for decoding the game
SIGN_EMPTY = " "
SIGN_BALL = "o"
SIGN_PLAYER = "x"

SPACE_SIZE = (20, 20)
ZOOM_SIZE = 10

ACTION_IDLE = "IDLE"
ACTION_LEFT = "LEFT"
ACTION_RIGHT = "RIGHT"

ACTIONS = [
    ACTION_IDLE,
    ACTION_LEFT,
    ACTION_RIGHT
]


class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate

        self.q_table = np.zeros((n_states, n_actions))

    def act(self, state, epsilon):
        random_int = random.uniform(0, 1)
        if random_int > epsilon:
            action = np.argmax(self.q_table[state])
        else:
            action = random.randint(0, self.n_actions - 1)
        return action

    def learn(self, state, action, reward, new_state, gamma):
        old_value = self.q_table[state][action]
        new_estimate = reward + gamma * max(self.q_table[new_state])
        self.q_table[state][action] = old_value + self.learning_rate * (new_estimate - old_value)


pygame.init()

size = (SPACE_SIZE[0] * ZOOM_SIZE, SPACE_SIZE[1] * ZOOM_SIZE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong")

rect_x = SPACE_SIZE[0] // 2
rect_y = SPACE_SIZE[1] - 1

rect_change_x = 0
rect_change_y = 0

rect_size_x = 5
rect_size_to_sides_x = rect_size_x // 2
rect_size_y = 1

ball_x = SPACE_SIZE[0] // 2
ball_y = 1

ball_change_x = 1
ball_change_y = 1
ball_size_to_sides = 1


def drawrect(screen, x, y):
    pygame.draw.rect(screen, RED,
                     [(x - rect_size_to_sides_x) * ZOOM_SIZE, y * ZOOM_SIZE,
                      ZOOM_SIZE * rect_size_x, ZOOM_SIZE])


def encode_state(ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y):
    return (ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y)


def reset():
    global ball_change_x, ball_change_y, ball_size_to_sides
    global ball_x, ball_y, rect_x, rect_y, rect_change_x, rect_change_y

    ball_change_x = 1
    ball_change_y = 1
    ball_size_to_sides = 1

    ball_x = SPACE_SIZE[0] // 2
    ball_y = 1

    rect_x = SPACE_SIZE[0] // 2
    rect_y = SPACE_SIZE[1] - 1

    rect_change_x = 0
    rect_change_y = 0


state_to_id = {}

num_states = SPACE_SIZE[0] * SPACE_SIZE[1] * SPACE_SIZE[0] * SPACE_SIZE[1] * 2 * 2
print(num_states)

agent = QLearningAgent(n_states=num_states, n_actions=3, learning_rate=1.0)

clock = pygame.time.Clock()


def play_episodes(n_episodes=10_000, max_epsilon=1.0, min_epsilon=0.05,
                  decay_rate=0.0001, gamma=0.99, learn=True, viz=False,
                  human=False, log=False):
    global ball_change_x, ball_change_y, ball_size_to_sides
    global ball_x, ball_y, rect_x, rect_y, rect_change_x, rect_change_y

    rewards = []
    epsilon_history = []

    for episode in tqdm(range(n_episodes)):
        done = False

        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-decay_rate * episode)

        total_reward = 0
        reset()

        state = encode_state(ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y)
        if state not in state_to_id:
            state_to_id[state] = len(state_to_id)

        while not done:
            reward = 0
            screen.fill(BLACK)

            # --------------------------------------
            # EVENT HANDLING FOR BOTH MODES (Q to quit)
            # --------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    done = True
            # --------------------------------------

            if done:
                break

            if not human:
                action = agent.act(state=state_to_id[state], epsilon=epsilon)
                action_name = ACTIONS[action]

                if action_name == ACTION_LEFT:
                    rect_change_x = -1
                elif action_name == ACTION_RIGHT:
                    rect_change_x = 1
                elif action_name == ACTION_IDLE:
                    rect_change_x = 0
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            done = True
                        elif event.key == pygame.K_LEFT:
                            rect_change_x = -1
                        elif event.key == pygame.K_RIGHT:
                            rect_change_x = 1
                    elif event.type == pygame.KEYUP:
                        if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                            rect_change_x = 0
                if done:
                    break

            rect_x += rect_change_x
            rect_y += rect_change_y

            if ball_x < 0:
                ball_x = 0
                ball_change_x *= -1
            elif ball_x > SPACE_SIZE[0]:
                ball_x = SPACE_SIZE[0]
                ball_change_x *= -1
            elif ball_y < 0:
                ball_y = 0
                ball_change_y *= -1
            elif ball_x + ball_size_to_sides >= rect_x - rect_size_to_sides_x and \
                    ball_x - ball_size_to_sides <= rect_x + rect_size_to_sides_x and \
                    ball_y == SPACE_SIZE[1] - 1:
                ball_change_y *= -1
                reward = 1
            elif ball_y > SPACE_SIZE[1] - 1:
                ball_change_y *= -1
                done = True
                reward = -1

            new_state = encode_state(ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y)
            if new_state not in state_to_id:
                state_to_id[new_state] = len(state_to_id)

            ball_x += ball_change_x
            ball_y += ball_change_y

            if rect_x - rect_size_to_sides_x < 0:
                rect_x = 0 + rect_size_to_sides_x
                reward = -1
                done = True
            if rect_x > SPACE_SIZE[0] - rect_size_to_sides_x - 1:
                rect_x = SPACE_SIZE[0] - rect_size_to_sides_x - 1
                reward = -1
                done = True

            if viz:
                pygame.draw.rect(screen, WHITE,
                                 [(ball_x - ball_size_to_sides) * ZOOM_SIZE,
                                  (ball_y - ball_size_to_sides) * ZOOM_SIZE,
                                  ZOOM_SIZE * ball_size_to_sides, ZOOM_SIZE * ball_size_to_sides])

                drawrect(screen, rect_x, rect_y)
                pygame.display.flip()
                clock.tick(60)

            if learn:
                agent.learn(state_to_id[state], action, reward, state_to_id[new_state], gamma)

            state = new_state
            total_reward += reward

        rewards.append(total_reward)
        epsilon_history.append(epsilon)

    return rewards, epsilon_history


rewards, epsilon_history = play_episodes(
    n_episodes=50_000, max_epsilon=1.0, min_epsilon=0.05, decay_rate=0.0001,
    gamma=0.95, learn=True, viz=False, human=False, log=False
)

plt.plot(epsilon_history)
plt.show()

plt.plot(rewards)
plt.show()

with open("agent.pkl", "wb") as f:
    pickle.dump(agent, f)
with open("state_to_id.pkl", "wb") as f:
    pickle.dump(state_to_id, f)

rewards, epsilon_history = play_episodes(
    1, max_epsilon=0, min_epsilon=0, decay_rate=0, gamma=0,
    learn=False, viz=True, log=True
)

plt.plot(epsilon_history)
plt.show()
plt.plot(rewards)
plt.show()

pygame.quit()
