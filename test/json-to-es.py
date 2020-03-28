import json


print('hello world1')
with open('test\demo.json', 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print(aa)

single_user_file = {
'id': 1,
	'profile': {
		'name': 'Pankaj Gurbani',
        'current title':'Data Scientist at Labatt Breweries of Canada',
        'location':'Toronto, Canada Area'
    },
	'experience': [{"company": "Beam Data", "Title": "Data Scientist (Client: Samsung Electronics Canada)", "Date": "5 mos"}, 
                    {"company": "Reliance Industries Limited", "Title": "Business Operations Analyst", "Date": "2 yrs 6 mos"}] 
    ,
	'skills': ["Data Science", "Business Strategy", "Business Intelligence (BI)"]
	,
	'interest': ["Bill Gates", "Machine Leaning"]
		
	,
	'education': [{"school": ["Management Development Institute"], "degree": ["Master of Business Administration - MBA"], "major": ["Operations, Marketing"]},
                  {"school": ["NIRMA UNIVERSITY"], "degree": ["B. Tech"], "major": ["Mechanical Engineering"]}]
}