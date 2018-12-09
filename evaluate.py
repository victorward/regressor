import sys

import numpy as np
import matplotlib.pyplot as plt


def compute_mse(out, res):
    return np.square(out - res).mean()


def compute_mad(out, res):
    return np.abs(out - res).max()


def plot(in_file, out, res, fileNo):
    if len(in_file.shape) != 1:
        return
    f1 = plt.scatter(in_file, out, color='r', s=5)
    f2 = plt.plot(in_file, res, 'b')
    plt.savefig("figure_{}".format(fileNo))
    plt.show()


def main():
    fileNo = sys.argv[1]
    out = np.loadtxt("out{}.txt".format(fileNo))
    res = np.loadtxt("res{}.txt".format(fileNo))
    in_file = np.loadtxt("in{}.txt".format(fileNo))
    mse = compute_mse(out, res)
    mad = compute_mad(out, res)
    print("Mean Square Error: {}".format(mse))
    print("Maximum Aboslute Difference: {}".format(mad))
    plot(in_file, out, res, fileNo)


if __name__ == "__main__":
    main()
