import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    for i in range(len(predictions)):
        error = net_worths[i] - predictions[i]

        cleaned_data.append((ages[i], net_worths[i], error))

    cleaned_data.sort(key=sortByErrorValue, reverse=False)

    return cleaned_data[:( len(cleaned_data) - math.trunc(len(cleaned_data) / 10) )]

def sortByErrorValue(array):
    return abs(array[2][0]) #error