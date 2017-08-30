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

print(len(enron_data))

count_poi = 0
max_total_payments = { 'name': '', 'money': 0}
have_salary = 0
have_email = 0
have_nan_value_of_total_payments = 0
count_of_poi_who_has_nan_value_of_total_payments = 0

for i in enron_data:
	# find person with max total payments
	if 'LAY' in i or 'SKILLING' in i or 'FASTOW' in i:
		if enron_data[i]['total_payments'] > max_total_payments['money']:
			max_total_payments['money'] = enron_data[i]['total_payments']
			max_total_payments['name'] = i

	# count all persons of interest
	if enron_data[i]['poi'] == True:
		count_poi += 1

	# count all persons who has valid salary value
	if enron_data[i]['salary'] != 'NaN':
		have_salary += 1

	# count all persons who has valid email address
	if enron_data[i]['email_address'] != 'NaN':
		have_email += 1

	if enron_data[i]['total_payments'] == 'NaN':
		have_nan_value_of_total_payments += 1

	if enron_data[i]['poi'] == True and enron_data[i]['total_payments'] == 'NaN':
		count_of_poi_who_has_nan_value_of_total_payments += 1


print(count_poi)

print(enron_data['PRENTICE JAMES']['total_stock_value'])

print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print(max_total_payments)

print(have_salary)

print(have_email)

print(have_nan_value_of_total_payments)

print(100 * have_nan_value_of_total_payments / len(enron_data))

print(100 * count_of_poi_who_has_nan_value_of_total_payments / len(enron_data))