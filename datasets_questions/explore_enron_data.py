#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Total people in enron data", len(enron_data)
# Could use keys() to get same result
# print "Total people in enron data ", len(enron_data.keys())
print "Total feature of one person", len(enron_data['METTS MARK'])

for name in ['Prentice James', 'Colwell Wesley', 'Skilling Jeffrey K']:
    print name + ":", enron_data[name.upper()]

poi = 0
have_salary = 0
have_email = 0
have_total_payments = 0
poi_total_payments = 0
for people in enron_data.keys():
    if enron_data[people]['poi']:
        poi += 1
        if enron_data[people]['total_payments'] != 'NaN':
            poi_total_payments += 1
    if enron_data[people]['salary'] != 'NaN':
        have_salary += 1
    if enron_data[people]['email_address'] != 'NaN':
        have_email += 1
    if enron_data[people]['total_payments'] != 'NaN':
        have_total_payments += 1

print "Total POI", poi
print "Available Salary", have_salary
print "Available Email", have_email
print "Available total_payments", have_total_payments, float(146-have_total_payments)/146
print "Available POI total_payments", poi_total_payments, float(146-poi_total_payments)/146

