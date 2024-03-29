from abc import ABC, abstractmethod

# Abstract class that is useful to check that the state manager is not specific to only Hex.
# HexStateManager implements these abstract methods.


class StateManager(ABC):
    @abstractmethod
    def copy_state_manager(self):
        pass

    @abstractmethod
    def get_legal_moves(self, player):
        pass

    @abstractmethod
    def make_move(self, move, player):
        pass

    @abstractmethod
    def make_random_move(self, player):
        pass

    @abstractmethod
    def generate_child_states(self, player):
        pass

    @abstractmethod
    def check_winning_state(self, player):
        pass
        
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_eval(self, winner):
        pass

    @abstractmethod
    def get_distribution_shape(self):
        pass
