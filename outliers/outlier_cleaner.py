#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ratio = 0.9
    keep_len = int(len(predictions)*ratio)
    ### your code goes here
    error = (net_worths - predictions) ** 2
    sorted_indices = np.argsort(error.T)[0]
    #raw_data = np.array([ages, net_worths, error])

    #print sorted_indices[:keep_len]
    #print error[sorted_indices[:keep_len]]
    #print raw_data[:,sorted_indices[:keep_len]]
    cleaned_data = zip(ages[sorted_indices[:keep_len]], net_worths[sorted_indices[:keep_len]], error[sorted_indices[:keep_len]])
    return cleaned_data

