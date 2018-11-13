class Options:
    def __init__(self, iterations=1000, learning_rate=0.2, max_polynomial_degree=4, divisions_quantity=6, proportion=5):
        self.divisions_quantity = divisions_quantity
        self.max_polynomial_degree = max_polynomial_degree
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.proportion = proportion
