# Board config
BOARD_SIZE = 5

# MCTS config
MCTS_DYNAMIC_SIMS = False
MCTS_DYNAMIC_SIMS_TIME = 0.1
MCTS_MIN_SIMULATIONS = 50

MTCS_SIMULATIONS = 1000
MTCS_C = 1.0
EPSILON = 1.0
EPSILON_DECAY = 0.998

# RL config
NUM_EPISODES = 500
DISPLAY_GAME_RL = True
DISPLAY_GAME_RL_INTERVAL = 1
REPLAY_BUFFER_SIZE = 1000
CHECK_WINNING_MOVES_RL = True

# ANN config
NN_TYPE = "cnn"
LEARNING_RATE = 0.001
NEURAL_NETWORK_DIMENSIONS = (512, 256)
ACTIVATION_FUNCTION = "relu"
OUTPUT_ACTIVATION_FUNCTION = "softmax"
ANN_OPTIMIZER = "Adam"
LOSS_FUNCTION = "categorical_crossentropy"
BATCH_SIZE = 128
NUM_EPOCHS = 5

# TOPP
MODEL_DIR = "models"
TOPP_TEMPERATURE = 0.8
TOPP_M = 11
TOPP_NUM_GAMES = 30
TOPP_VERBOSE = True
TOPP_DISPLAY_GAMES = True
