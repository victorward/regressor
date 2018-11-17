import utils.utils as utils


class Model:
    def __init__(self, degree, alpha, options):
        self.degree = degree
        self.alpha = alpha
        self.options = options
        self.mistake = None
        self.mistakes = []

    def __str__(self) -> str:
        return 'degree\t{}\nalpha\t{}\nmistake\t{}\nmistakes\t{}\n'.format(
            self.degree, self.alpha, self.mistake, self.mistakes
        )
        # return 'degree\t{}\nalpha\t{}\nmistake\t{}\nmistakes\t{}\noptions:\n{}\n'.format(
        #     self.degree, self.alpha, self.mistake, self.mistakes, self.options
        # )

    def calc_division_mistake(self, division, teta, set_points_min_max):
        linear_train = utils.convert_to_linear(teta, division['train_set'])
        linear_validation = utils.convert_to_linear(teta, division['validation_set'])
        #  hmm
        linear_train_with_1 = utils.add_1_at_start(linear_train)
        linear_validation_with_1 = utils.add_1_at_start(linear_validation)

        new_teta = self.gradient(linear_train_with_1)
        desired_results = [point[-1] for point in division['validation_set']]
        columns_linear_validation = utils.get_points_by_column(linear_validation_with_1)
        calculated_results = utils.get_current_value(new_teta, columns_linear_validation)
        unscaled_results = utils.unscale_results(calculated_results, set_points_min_max)
        unscaled_desired_results = utils.unscale_results(desired_results, set_points_min_max)

        return utils.calculate_mistake(unscaled_results, unscaled_desired_results)

    def gradient(self, points):
        return utils.gradient(points, self.options, self.alpha)

