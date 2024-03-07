class GameState:
    def __init__(self):
        # 0: Empty, 1: X, 2: O
        self.game_state = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

    def check(self):
        # return => 0: No winner, 1: X, 2: O
        win_states = [
            # game_state indexes
            (0, 1, 2), (3, 4, 5), (6, 7, 8,),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for state in win_states:
            if (   self.game_state[state[0]]
                == self.game_state[state[1]]
                == self.game_state[state[2]]
            ):
                return self.game_state[state[0]]
        return 0
    
    def update(self, tile, value):
        self.game_state[tile] = value
    
    def reset(self):
        self.game_state = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]
