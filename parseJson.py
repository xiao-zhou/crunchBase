

import json
from pprint import pprint
json_data=open('facebook.json')

data = json.load(json_data)
employee_num = data['number_of_employees']
company_name = data['name']
funding_rounds = data['funding_rounds']
for(item in funding_rounds):
	item['raised_amount']
	investment = item['investment']
	if(investment['person'] == null)

pprint(data['total_money_raised'])
json_data.close()