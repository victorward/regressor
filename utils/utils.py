import itertools
import random
import operator as operator


def get_column_max_min(points):
    columns = [column(points, idx) for idx, val in enumerate(points[0])]
    min_points = [min(col) for col in columns]
    max_points = [max(col) for col in columns]

    return {'max_points': max_points, 'min_points': min_points}


def scale_points(points, column_max_min):
    scaled = []
    for p in points:
        point = []
        for idx, val in enumerate(p):
            point.append((val - column_max_min['min_points'][idx]) / (
                    column_max_min['max_points'][idx] - column_max_min['min_points'][idx]))
        scaled.append(point)

    return scaled


def unscale_results(results, column_max_min):
    min = column_max_min['min_points'][-1]
    max = column_max_min['max_points'][-1]

    return [(res - min / (min - max)) * (max - min) for res in results]


def column(matrix, i):
    return [row[i] for row in matrix]


def get_points_by_column(matrix):
    points = []
    for i in range(len(matrix[0])):
        points.append(column(matrix, i))

    return points


def create_alphas():
    return [10 ** x for x in range(-4, 2)]


def repeat_value(value, times):
    return [value] * times


def get_current_value(teta, columns):
    current_value = [c * teta[-1] for c in columns[0]]
    for i in range(1, len(columns) - 1):
        multiplier = teta[i - 1]
        component = [value * multiplier for value in columns[i]]
        current_value = list(map(operator.add, current_value, component))

    return current_value


def sum_mistake(current_value, desired_value, size):
    return sum([mistake ** 2 for mistake in list(map(operator.sub, current_value, desired_value))]) / size


def get_gradient_free_expression(columns, current_value, desired_value, size, i):
    return -sum(map(operator.mul, columns[i], list(map(operator.sub, desired_value, current_value)))) * 1 / size


def get_gradient_new_teta(teta, teta_tmp, columns, current_value, desired_value, size, alpha, learning_rate, i):
    gradient = get_gradient_free_expression(columns, current_value, desired_value, size, i)
    gradient_lambda = gradient + alpha / size * teta[i - 1]
    teta_tmp[i - 1] = teta[i - 1] - learning_rate * gradient_lambda

    return teta_tmp


def convert_to_linear(teta, points):
    points_with_1_at_start = add_1_at_start(points)
    linear = []
    for point in points_with_1_at_start:
        new = []
        for t in teta:
            product = 1
            point_variables = []
            if all(x == 0 for x in t['variables']):
                continue
            for idx, val in enumerate(t['variables']):
                point_variables.append(point[val])
                product = product * point[val]

            new.append(product)

        new.append(point[-1])
        linear.append(new)

    return linear


def gradient(points, options, alpha):
    n = len(points[0]) - 2
    teta = repeat_value(1, n + 1)
    mistake_sum = 0
    columns = get_points_by_column(points)
    desired_value = columns[n + 1]
    size = len(columns[1])  # moze buty 0

    for i in range(options.max_iter):
        teta_tmp = teta
        mistake_sum_tmp = mistake_sum
        current_value = get_current_value(teta, columns)
        mistake_sum = sum_mistake(current_value, desired_value, size)
        if mistake_sum <= mistake_sum_tmp:
            options.learning_rate = options.learning_rate * 1.1
            # options.learning_rate = options.learning_rate * (1 + float(options.learning_rate))
        else:
            options.learning_rate = options.learning_rate * 0.9
            # options.learning_rate = options.learning_rate * (1 - float(options.learning_rate))

        gradient = get_gradient_free_expression(columns, current_value, desired_value, size, 0)
        gradient_alpha = gradient + alpha / size * teta[-1]
        teta_tmp[-1] = teta[-1] - options.learning_rate * gradient_alpha
        for p in range(1, len(columns) - 1):
            teta = get_gradient_new_teta(teta, teta_tmp, columns, current_value, desired_value, size,
                                         alpha, options.learning_rate, p)

    return teta


def create_random_division(points, percents):
    train_set = []
    validation_set = []
    data_size = len(points)
    train_set_size = int(data_size * percents)
    for index in range(data_size):
        if index < train_set_size:
            train_set.append(points[index])
        else:
            validation_set.append(points[index])

    return {'train_set': train_set, 'validation_set': validation_set}


def create_ordered_divisions(divisions_quantity, points, proportion):
    divisions = []
    for i in range(divisions_quantity):
        divisions.append(create_random_division(points, proportion))

    return divisions


def generate_polynomial_with_teta(dimension, degree):
    dimensions = range(dimension, -1, -1)
    combinations = itertools.combinations_with_replacement(dimensions, degree)

    return [{'variables': list(c), 'multiplier': random.uniform(-1.0, 1.0)} for c in combinations]


def generate_random_polynomials(dimension, max_degree):
    polynomials = []
    for degree in range(max_degree):
        polynomials.append(generate_polynomial_with_teta(dimension, degree))

    return polynomials


def add_1_at_start(points):
    return [[1] + point for point in points]


def calculate_mistake(actual, desired):
    return sum([(actual[x] - desired[x]) ** 2 for x in range(len(actual))]) ** 0.5


def sort_models_by_mistake(models):
    models.sort(key=lambda x: x.mistake)


def show_models(models):
    for m in models:
        print(m)


def print_results(result):
    print(*result, sep='\n')
