class Hyperparam(object):
    def __init__(self, batch_size, learning_rate, optimizer):
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.optimizer = optimizer

    def __repr__(self):
        return "hyperparameters:\n" + \
            "batch_size: " + str(self.batch_size) + '\n' \
            "learning_rate: " + str(self.learning_rate) + '\n' \
            "optimizer: " + str(self.optimizer)
