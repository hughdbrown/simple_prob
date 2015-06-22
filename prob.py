import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt


def show_boxplot(test_data):
    plt.boxplot(test_data)
    plt.show()


def save_boxplot(test_data):
    plt.boxplot(test_data)
    plt.savefig("boxplot.png")


def show_histogram(test_data):
    plt.hist(test_data, histtype='bar')
    plt.show()


def show_QQ(test_data):
    graph1 = stats.probplot(test_data, dist="norm", plot=plt)
    plt.show()
