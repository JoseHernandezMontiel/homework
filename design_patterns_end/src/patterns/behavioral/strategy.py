# Focus Points the main method creates the Strategy
import abc

class Strategy(abc.ABC):

    def run_algorithm(self, array):
        raise Exception("I am an interface")


class MergeSort:

    def run_algorithm(self, array):
        print("Sorting by Merge Sort")
        return sorted(array)


class QuickSort:

    def run_algorithm(self, array):
        print("Sorting by Quick Sort")
        return sorted(array)


class ArraySorter:

    def __init__(self, strategy, array):
        self.strategy = strategy
        self.array = array

    def run_algorithm(self):
        return self.strategy.run_algorithm(self.array)