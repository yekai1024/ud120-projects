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

Skilling Jeffrey K: {'salary': 1111258, 'to_messages': 3627, 'deferral_payments': 'NaN', 'total_payments': 8682716, 'exercised_stock_options': 19250000, 'bonus': 5600000, 'restricted_stock': 6843672, 'shared_receipt_with_poi': 2042, 'restricted_stock_deferred': 'NaN', 'total_stock_value': 26093672, 'expenses': 29336, 'loan_advances': 'NaN', 'from_messages': 108, 'other': 22122, 'from_this_person_to_poi': 30, 'poi': True, 'director_fees': 'NaN', 'deferred_income': 'NaN', 'long_term_incentive': 1920000, 'email_address': 'jeff.skilling@enron.com', 'from_poi_to_this_person': 88}

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

