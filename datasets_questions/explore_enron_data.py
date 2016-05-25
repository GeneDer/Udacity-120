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

print len(enron_data)

print len(enron_data.values()[0])

print sum([enron_data[i]["poi"] for i in enron_data])

print enron_data['PRENTICE JAMES']['total_stock_value']

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

lay = enron_data['LAY KENNETH L']['total_payments']
skilling = enron_data['SKILLING JEFFREY K']['total_payments']
fastow = enron_data['FASTOW ANDREW S']['total_payments']
if lay > skilling and lay > fastow:
    print 'Lay: %s'%lay
elif skilling > lay and skilling > fastow:
    print 'Skilling: %s'%skilling
else:
    print 'Fastow: %s'%fastow

countSalary = 0
countEmail = 0
countTotalPayment = 0
for i in enron_data:
    if enron_data[i]['salary'] != 'NaN':
        countSalary += 1
    if enron_data[i]['email_address'] != 'NaN':
        countEmail += 1
    if enron_data[i]['total_payments'] == 'NaN':
        countTotalPayment += 1
print countSalary, countEmail
print countTotalPayment, float(countTotalPayment)/len(enron_data)*100