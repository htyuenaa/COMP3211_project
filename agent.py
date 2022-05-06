from base import (BaseAgent, action_dict, move, TIMEOUT)
from func_timeout import func_set_timeout


##################################################################################
# Here is a demo agent.                                                          #
# You can implement any helper functions.                                        #
# You must not remove the set_timeout restriction.                               #
# You can start your code any where but only the get_action() will be evaluated. #
##################################################################################


class MyAgent(BaseAgent):
    # passed back from controller
    def __init__(self, name, env):
        super().__init__(name, env)
        self.path = None
        self.time = -1

    def reset_time(self):
        self.time = -1

    @func_set_timeout(TIMEOUT)
    def get_action(self, game_state=None):
        # TODO: you may want to start here
        # Feel free erase all the demo code above
        self.time += 1
        for action in action_dict:
            if move(game_state[self.name], action) == self.path[self.time]:
                return action
        return None
