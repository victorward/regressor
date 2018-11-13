# program -t set.txt < in.txt > out.txt
from utils.files_handler import FilesHandler
from utils.options import Options
import utils.utils as utils


def apply_calculations(options, set_points):
    dimension = len(set_points[0]) - 1
    random_polynomials = utils.generate_random_polynomials(dimension, options.max_polynomial_degree)
    alphas = utils.create_alphas()
    calculations = []
    for k in range(2, options.max_polynomial_degree):
        polynomia_teta = random_polynomials[k]
        print("polynomia_teta \n{}".format(polynomia_teta))


def start():
    options = Options()
    files_handler = FilesHandler()
    set_points = files_handler.get_points_from_file(files_handler.get_set_file_from_options())
    test_points = files_handler.get_test_points_from_stdin()

    apply_calculations(options, set_points)

    set_points_min_max = utils.get_column_max_min(set_points)
    scaled_set = utils.scale_points(set_points, set_points_min_max)
    divisions = utils.create_ordered_divisions(options.divisions_quantity, scaled_set, options.train_percents)

    return 0


if __name__ == "__main__":
    start()
