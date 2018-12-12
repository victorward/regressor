# program -t set.txt < in.txt > out.txt
# program -t set.txt -i in.txt > out.txt
from utils.files_handler import FilesHandler
from utils.model import Model
from utils.options import Options
import utils.utils as utils


def find_best_model(options, points_min_max, scaled_points, random_polynomials):
    divisions = utils.create_ordered_divisions(options.divisions_quantity, scaled_points, options.train_percents)
    alphas = utils.create_alphas()
    models = []
    for degree in range(2, options.max_polynomial_degree):
        polynomial_with_teta = random_polynomials[degree]
        for alpha in alphas:
            model = Model(degree, alpha, options)
            mistake = 0
            for division in divisions:
                division_mistake = model.calc_division_mistake(division, polynomial_with_teta, points_min_max)
                mistake += division_mistake
                model.mistakes.append(mistake)
            model.mistake = mistake
            models.append(model)

    utils.sort_models_by_mistake(models)
    # utils.show_models(models)

    return models[0]


def find_best_alpha(options, best_model, random_polynomials, scaled_set_points, scaled_test_points, points_min_max):
    teta = random_polynomials[best_model.degree]
    linear_set_points = utils.convert_to_linear(teta, scaled_set_points)
    linear_test_points = utils.convert_to_linear(teta, scaled_test_points)
    linear_set_points_with_1 = utils.add_1_at_start(linear_set_points)
    linear_test_points_with_1 = utils.add_1_at_start(linear_test_points)
    new_teta = utils.gradient(linear_set_points_with_1, options, best_model.alpha)
    linear_test_points_with_1_columns = utils.get_points_by_column(linear_test_points_with_1)
    result = utils.get_current_value(new_teta, linear_test_points_with_1_columns)
    unscaled = utils.unscale_results(result, points_min_max)

    return unscaled


def apply_calculations(options, set_points, test_points):
    dimension = len(set_points[0]) - 1
    random_polynomials = utils.generate_random_polynomials(dimension, options.max_polynomial_degree)

    set_points_min_max = utils.get_column_max_min(set_points)
    scaled_set_points = utils.scale_points(set_points, set_points_min_max)
    scaled_test_points = utils.scale_points(test_points, set_points_min_max)

    best_model = find_best_model(options, set_points_min_max, scaled_set_points, random_polynomials)
    best_alpha = find_best_alpha(options, best_model, random_polynomials, scaled_set_points, scaled_test_points,
                                 set_points_min_max)

    utils.print_results(best_alpha)


def start():
    # options = Options(max_iter=6000, learning_rate=0.01, max_polynomial_degree=7,
    #                   divisions_quantity=7, train_percents=0.9)
    # options = Options(max_iter=4000, learning_rate=0.001, max_polynomial_degree=6,
    #                   divisions_quantity=7, train_percents=0.8)
    options = Options(max_iter=9000, learning_rate=0.001, max_polynomial_degree=6,
                      divisions_quantity=2, train_percents=0.8)
    files_handler = FilesHandler()
    set_points = files_handler.get_points_from_file(files_handler.get_set_file_from_options())
    test_points = files_handler.get_test_points_from_stdin()

    apply_calculations(options, set_points, test_points)
    return 0


if __name__ == "__main__":
    start()
