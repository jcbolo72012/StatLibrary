import math

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

