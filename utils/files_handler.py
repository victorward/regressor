import optparse
import sys


class FilesHandler:
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-t', dest='set_file')
        parser.add_option('-i', dest='test_file')
        self.options, self.args = parser.parse_args()

    @staticmethod
    def get_points_from_file(filename):
        points = []
        file = open(filename, 'r')
        for point in file:
            points.append([float(x) for x in point.split(' ')])

        return points

    def get_set_file_from_options(self):
        return self.options.set_file

    def get_test_points_from_stdin(self):
        if self.options.test_file:
            return self.get_points_from_file(self.options.test_file)

        points = []
        for line in sys.stdin:
            points.append([float(x) for x in line.split(' ')])

        return points
