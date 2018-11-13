class Model:
    def __init__(self, polynomial_with_teta, alpha):
        self.polynomial_with_teta = polynomial_with_teta
        self.alpha = alpha
        self.error = None
        self.errors = []

    def __str__(self) -> str:
        return 'polynomial_with_teta\t{}\nalpha\t{}\nerror\t{}\nerrors\t{}\n'.format(
            self.polynomial_with_teta, self.alpha, self.error, self.errors
        )

    # def calc_division_mistake(self, division, teta, alpha):

    def convert_to_linear(self, teta, points):
