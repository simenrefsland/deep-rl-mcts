# Board config
BOARD_SIZE = 3

# MCTS config
NUM_EPISODES = 200
MCTS_DYNAMIC_SIMS = False
MCTS_MIN_SIMULATIONS = 200
MTCS_SIMULATIONS = 1000
MTCS_C = 1.0
MCTS_VERBOSE = True
EPSILON = 1.0
EPSILON_DECAY = 0.99

# RL config
DISPLAY_GAME_RL = True


# ANN config
LEARNING_RATE = 0.001
NEURAL_NETWORK_DIMENSIONS = (128, 64)
ACTIVATION_FUNCTION = "relu"
OUTPUT_ACTIVATION_FUNCTION = "softmax"
ANN_OPTIMIZER = "Adam"
LOSS_FUNCTION = "categorical_crossentropy"
SAVE_INTERVAL = 10
BATCH_SIZE = 128

# CNN config
NUM_FILTERS = 32
NUM_CONV_LAYERS = 2

# TOPP
M_ANN = 0
NUM_GAMES_TOPP = 0
TOPP_VERBOSE = True
