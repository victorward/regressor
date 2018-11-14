# program -t set.txt < in.txt > out.txt
from utils.files_handler import FilesHandler
from utils.model import Model
from utils.options import Options
import utils.utils as utils


def apply_calculations(options, set_points, test_points):
    dimension = len(set_points[0]) - 1
    set_points_min_max = utils.get_column_max_min(set_points)

    random_polynomials = utils.generate_random_polynomials(dimension, options.max_polynomial_degree)
    scaled_set = utils.scale_points(set_points, set_points_min_max)
    divisions = utils.create_ordered_divisions(options.divisions_quantity, scaled_set, options.train_percents)

    alphas = utils.create_alphas()
    calculations = []
    for degree in range(2, options.max_polynomial_degree):
        polynomial_with_teta = random_polynomials[degree]
        # print("polynomia_teta from random \n{}".format(polynomia_teta))
        for alpha in alphas:
            model = Model(degree, alpha)
            for division in divisions:
                mistake = model.calc_division_mistake(division, polynomial_with_teta)


def start():
    options = Options()
    files_handler = FilesHandler()
    set_points = files_handler.get_points_from_file(files_handler.get_set_file_from_options())
    test_points = files_handler.get_test_points_from_stdin()

    apply_calculations(options, set_points, test_points)
    return 0


if __name__ == "__main__":
    start()
