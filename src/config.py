# Board config
BOARD_SIZE = 7
CLASSIC_DISPLAY = True
SWITCH_RULE_ALLOWED = True

# MCTS config
MCTS_DYNAMIC_SIMS_TIME = 4.0
MCTS_MIN_SIMULATIONS = 2000
MTCS_C = 1.3
EPSILON = 1.0
EPSILON_DECAY = 0.99
EPSILON_CRITIC = 2.0
EPSILON_DECAY_CRITIC = 0.996

# RL config
NUM_EPISODES = 500
DISPLAY_GAME_RL = True
DISPLAY_GAME_RL_INTERVAL = 10
REPLAY_BUFFER_SIZE = 2048
MINI_BATCH_SIZE = 256
SAVE_INTERVAL = 50
SELECT_BEST_MOVE_RL = True

# ANN config
LEARNING_RATE = 0.001
CNN_FILTERS = (64, 64, 64, 64, 64)
ACTIVATION_FUNCTION = "relu"
OUTPUT_ACTIVATION_FUNCTION_ACTOR = "softmax"
OUTPUT_ACTIVATION_FUNCTION_CRITIC = "tanh"
ANN_OPTIMIZER = "Adam"
LOSS_FUNCTION_ACTOR = "categorical_crossentropy"
LOSS_FUNCTION_CRITIC = "mse"
NUM_EPOCHS = 5
BRIDGE_FEATURES = False
USE_CRITIC = False

# TOPP
MODEL_DIR = "models/2023-12-30_16-09-29"
TOPP_TEMPERATURE = 1.0
TOPP_NUM_GAMES = 30
TOPP_VERBOSE = True
TOPP_DISPLAY_GAMES = True
