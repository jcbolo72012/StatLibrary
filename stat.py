import math
import random

#### Section 1: Measures of Variance and Central Tendancy
## mean, median, mode, standard variance, standard deviation, and confidence interval
def mean(data):
    """The mean or average of a set of data is the sum of all data
        points divided by the amount of data points.
    """
    if not isinstance(data, list):
        raise Error("input must be of type list")
        return
    return sum(data)/len(data)

def standard_variance(data):

    """ The standard variance is the average distance from each
        data point to the mean of the data set
    """

    if not isinstance(data, list):
        raise Error("input must be of type list")
        return
    return (sum([x*x for x in data])-sum(data)*mean(data))/(len(data)-1)

def standard_deviation(data):
    if not isinstance(data, list):
        raise Error("input must be of type list")
        return
    return math.sqrt(standard_variance(data))

def confidence_interval(data):
    if not isinstance(data, list):
        raise Error("input must be of type list")
        return
    standard_deviation(data)/math.sqrt(len(data))

def median(data):
    """ Finds the median using Tony Hoare's recursive quickselect algorithm
        This method picks the appropriate way to call the recursive method based on
        whether the dataset has an even or odd number of members

        Average of O(n) time
    """
    pivot_fn = random.choice
    if len(data) % 2 == 1:  # case for datasets of even length
        return quickselect(data, len(data) // 2, pivot_fn) 
    else: # case for odd length
        0.5 * (quickselect(data, len(data) / 2 - 1, pivot_fn) + quickselect(data, len(data) / 2, pivot_fn))



def quickselect(data, index, pivot_fn):
    if len(data) == 1:
        assert index == 0
        return data[0]

    pivot = pivot_fn(data)

    less = [x for x in data if x<pivot] # all points less than the chosen pivot
    greater = [x for x in data if x>pivot] # all points greater than the chosen pivot
    equal = [x for x in data if x == pivot] # all points equal to the chosen pivot

    if index < len(less): # if 
        return quickselect(less, index, pivot_fn)
    elif index < len(less) + len(equal):
        return equal[0]
    else:
        return quickselect(greater, index - (len(less) + len(equal)), pivot_fn)

print(median([5,6,3,2,4,7,1]))