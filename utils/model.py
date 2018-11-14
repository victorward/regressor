class Model:
    def __init__(self, degree, alpha):
        self.degree = degree
        self.alpha = alpha
        self.error = None
        self.errors = []

    def __str__(self) -> str:
        return 'degree\t{}\nalpha\t{}\nerror\t{}\nerrors\t{}\n'.format(
            self.degree, self.alpha, self.error, self.errors
        )

    def calc_division_mistake(self, division, teta):
        # self.alpha
        lin_conv = self.convert_to_linear(teta, division['train_set'])

    def convert_to_linear(self, teta, points):
        print('teta {}'.format(teta))
        return 0
