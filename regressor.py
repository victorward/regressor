# program -t set.txt < in.txt > out.txt
from options import Options
import utils.utils as utils


def start():
    options = Options()
    set_points = utils.get_points_from_file(utils.get_set_file_from_options())
    test_points = utils.get_test_points_from_stdin()
    dimension = len(set_points[0]) - 1
    set_points_min_max = utils.get_column_max_min(set_points)
    scaled_set = utils.scale_points(set_points, set_points_min_max)
    divisions = utils.create_ordered_divisions(options.divisions_quantity, scaled_set, options.proportion)
    print(set_points)
    print(divisions)

    return 0


if __name__ == "__main__":
    start()
