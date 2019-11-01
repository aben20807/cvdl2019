class Hyperparam(object):
    def __init__(self, batch_size, learning_rate, optimizer, loss_fn, pretrained_model_path):
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.pretrained_model_path = pretrained_model_path

    def __repr__(self):
        return "hyperparameters:\n" + \
            "batch_size: " + str(self.batch_size) + '\n' \
            "learning_rate: " + str(self.learning_rate) + '\n' \
            "optimizer: " + str(self.optimizer.__name__)
