import utils.utils as utils


class Model:
    def __init__(self, degree, lmbda, options):
        self.degree = degree
        self.lmbda = lmbda
        self.options = options
        self.mistake = None
        self.mistakes = []

    def __str__(self) -> str:
        return 'degree\t{}\nlmbda\t{}\nmistake\t{}\nmistakes\t{}\n'.format(
            self.degree, self.lmbda, self.mistake, self.mistakes
        )

    def calc_division_mistake(self, division, teta):
        linear_train = utils.convert_to_linear(teta, division['train_set'])
        linear_validation = utils.convert_to_linear(teta, division['validation_set'])
        linear_train_1 = utils.add_1(linear_train)
        linear_validation_1 = utils.add_1(linear_validation)

        new_teta = utils.gradient(linear_train_1, self.options.max_iter, self.options.learning_rate, self.lmbda)
        desired_results = [point[-1] for point in division['validation_set']]
        columns_linear_validation = utils.get_points_by_column(linear_validation_1)
        calculated_results = utils.get_current_value(new_teta, columns_linear_validation)

        return utils.calculate_mistake(calculated_results, desired_results)
