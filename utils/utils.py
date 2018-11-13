import optparse
import sys


def get_points_from_file(filename):
    points = []
    file = open(filename, 'r')
    for point in file:
        coordinates = [float(x) for x in point.split(' ')]
        points.append(coordinates)

    return points


def get_set_file_from_options():
    parser = optparse.OptionParser()
    parser.add_option('-t', dest='set_file')
    options, args = parser.parse_args()

    return options.set_file


def get_test_points_from_stdin():
    points = []
    while True:
        try:
            coordinates = [float(x) for x in sys.stdin.readLine().split(' ')]
            points.append(coordinates)
        except:
            return points


def get_column_max_min(points):
    dimension = len(points[0])
    max_points = [-1000] * dimension
    min_points = [1000] * dimension
    for point in points:
        for dim in range(dimension):
            if point[dim] > max_points[dim]:
                max_points[dim] = point[dim]
            if point[dim] < min_points[dim]:
                min_points[dim] = point[dim]

    return {'max_points': max_points, 'min_points': min_points}


def scale_points(points, column_max_min):
    zipped = list(zip(column_max_min['min_points'], column_max_min['max_points']))
    scaled = []
    for p in points:
        point = []
        for i in range(len(p)):
            a = zipped[i][0]
            b = zipped[i][1]
            scaled_point = p[i] / (b - a) - a / (b - a)
            point.append(scaled_point)

        scaled.append(point)

    return scaled


def create_random_division(points, proportion):
    train_set = []
    validation_set = []
    for index in range(len(points)):
        if index % proportion != 0:
            train_set.append(points[index])
        else:
            validation_set.append(points[index])

    return {'train_set': train_set, 'validation_set': validation_set}


def create_ordered_divisions(divisions_quantity, points, proportion):
    divisions = []
    for i in range(divisions_quantity):
        divisions.append(create_random_division(points, proportion))

    return divisions
