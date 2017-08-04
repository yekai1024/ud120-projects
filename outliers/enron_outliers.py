#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
"""
TOTAL {'salary': 26704229, 'to_messages': 'NaN', 'deferral_payments': 32083396, 'total_payments': 309886585, 'exercised_stock_options': 311764000, 'bonus': 97343619, 'restricted_stock': 130322299, 'shared_receipt_with_poi': 'NaN', 'restricted_stock_deferred': -7576788, 'total_stock_value': 434509511, 'expenses': 5235198, 'loan_advances': 83925000, 'from_messages': 'NaN', 'other': 42667589, 'from_this_person_to_poi': 'NaN', 'poi': False, 'director_fees': 1398517, 'deferred_income': -27992891, 'long_term_incentive': 48521928, 'email_address': 'NaN', 'from_poi_to_this_person': 'NaN'}
Record 'TOTAL', index 67 should be removed from the dictionary before featureFormat
"""

data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)

#print data_dict
### your code below
highest = 0
abnormal_bonus = []
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if highest < salary:
        highest = salary
    if bonus > 5000000:
        abnormal_bonus.append(bonus)

print highest, abnormal_bonus
for people in data_dict:
    if data_dict[people]['salary'] == highest:
        print "Highest Salary", people, data_dict[people]
    if data_dict[people]['bonus'] in abnormal_bonus:
        print "Bonus > 5,000,000", people, data_dict[people]

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

