from pymongo import MongoClient
from bson import ObjectId
dbName = "aggregation"
client = MongoClient('mongodb://localhost:27017/')
db = client[dbName]

testNames = ['Cognitive Skill (Quant-Verbal-Reasoning) - 3rd/4th Year - Baseline Test']

topic1 = [
	{
	    '$unwind': '$QA'
	},
	{
	    '$match':{

                "user" : ObjectId("5bb18e50a7de887692545e31"),
	    	'QA.status': 1,
                'QA.topic.name' : "Syllogism"
	    }
	},
	{
	    '$project':{
	        'question': '$QA.question',
	    	'timeSpent': '$QA.timeEslapse',
	    	'status': '$QA.status',
	    	'user': '$user'
	    }
	}
]


topic2 = [
	{
	    '$unwind': '$QA'
	},
	{
	    '$match':{

                "user" : ObjectId("5bb18e50a7de887692545e31"),
	    	'QA.status': 2,
                'QA.topic.name' : "Syllogism"
	    }
	},
	{
	    '$project':{
	        'question': '$QA.question',
	    	'timeSpent': '$QA.timeEslapse',
	    	'status': '$QA.status',
	    	'user': '$user'
	    }
	}
]
topic1 = list(db.attemptdetails.aggregate(topic1))
topic2 = list(db.attemptdetails.aggregate(topic2))
len1 = len(topic1)
len2 = len(topic2)
sum1 = 0
for i in range(len1):
	check = topic1[i]
	print(check["status"])
	sum1 = sum1 + 1


sum2 = 0
for i in range(len2):
	check = topic2[i]
	print(check["status"])
	sum2 = sum2 + 1

if sum1 > no_of_questions:
	print("Less improvement")
	tp = "Less improvement"
else:
	print("More improvement")
	tp = "More improvement"

tp = message	
tp.to_excel(writer, sheet_name='weakest_topics', index=False)
filename = baseDir + slugify(joiner.join(centerNames)) + "_" + section + "_summary_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + ".json"
json.dump(summary, open(filename, 'w'))