import itertools
import random


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


def column(matrix, i):
    return [row[i] for row in matrix]


def create_alphas():
    return [10 ** x for x in range(-4, 2)]


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


# teta czy multiplayer
def generate_polynomial_with_teta(dimension, degree):
    dimensions = range(dimension, -1, -1)
    combinations = itertools.combinations_with_replacement(dimensions, degree)
    # polynomial_with_teta = []
    # for x in combinations:
    #     ls = list(x)
    #     ls.append(random.uniform(-1.0, 1.0))
    #     polynomial_with_teta.append(ls)

    return [{'teta': list(c), 'multiplier': random.uniform(-1.0, 1.0)} for c in combinations]


def generate_random_polynomials(dimension, max_degree):
    polynomials = []
    for degree in range(max_degree):
        polynomials.append(generate_polynomial_with_teta(dimension, degree))

    return polynomials
