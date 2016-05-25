#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    err = []
    for i in range(len(predictions)):
        err.append(abs(predictions[i] - net_worths[i]))
    errThreshold = sorted(err)[9*len(err)/10]
    for i in range(len(predictions)):
        if err[i] < errThreshold:
            cleaned_data.append((ages[i], net_worths[i], err[i]))
    
    return cleaned_data

