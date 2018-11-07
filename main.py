# program -t set.txt < in.txt > out.txt
import getopt
import sys


def start(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:")
        input_file = sys.stdin
    except getopt.GetoptError:
        print('program -t set.txt < in.txt > out.txt')
        sys.exit(2)

    print(opts)
    print(input_file)

    for line in input_file:
        print("line {}".format(line.strip()))

    print("Ned")

    return 0


if __name__ == "__main__":
    start(sys.argv[1:])
