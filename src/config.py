# Board config
BOARD_SIZE = 5

# MCTS config
MCTS_DYNAMIC_SIMS = True
MCTS_MIN_SIMULATIONS = 1000
MTCS_SIMULATIONS = 1000
MTCS_C = 1.0
EPSILON = 1.0
EPSILON_DECAY = 0.998

# RL config
NUM_EPISODES = 200
DISPLAY_GAME_RL = False
REPLAY_BUFFER_SIZE = 700
CHECK_WINNING_MOVES = False

# ANN config
LEARNING_RATE = 0.001
NEURAL_NETWORK_DIMENSIONS = (128, 64)
ACTIVATION_FUNCTION = "relu"
OUTPUT_ACTIVATION_FUNCTION = "softmax"
ANN_OPTIMIZER = "Adam"
LOSS_FUNCTION = "categorical_crossentropy"
SAVE_INTERVAL = 10
BATCH_SIZE = 128
NUM_EPOCHS = 5

# CNN config
CNN_DIMENSIONS = (16, 32)

# TOPP
MODEL_DIR = "models_5x5_topp_best"
TOPP_TEMPERATURE = 0.8
TOPP_M = 5
TOPP_NUM_GAMES = 100
TOPP_VERBOSE = True
