class Options:
    def __init__(self, max_iter=1000, learning_rate=0.2, max_polynomial_degree=6, divisions_quantity=6,
                 train_percents=0.9, alpha_learning_rate=0.01, alpha_iterations=11 ** 5):
        self.divisions_quantity = divisions_quantity
        self.max_polynomial_degree = max_polynomial_degree
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.train_percents = train_percents
        self.alpha_learning_rate = alpha_learning_rate
        self.alpha_iterations = alpha_iterations

    def __str__(self) -> str:
        return 'divisions_quantity\t{}\nmax_polynomial_degree\t{}\nlearning_rate\t{}\nmax_iter\t{}\ntrain_percents\t{}\n' \
            .format(self.divisions_quantity, self.max_polynomial_degree, self.learning_rate, self.max_iter,
                    self.train_percents)
