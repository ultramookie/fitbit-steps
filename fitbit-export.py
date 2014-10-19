import json
import fitbit
import os.path
from datetime import date
 
consumer_key = ''
consumer_secret = ''
user_key = ''
user_secret = ''
jsondir = 'fitbit-json/'
# your user_id, you can get from URL for your profile
uid=''
# actually the first day that you started using fitbit in the format YYYY-MM-DD
end_date=''

d = date.today()
today = str(d.isoformat())
 
#Setup an unauthorised client (e.g. with no user)
unauth_client = fitbit.Fitbit(consumer_key, consumer_secret)
 
authd_client = fitbit.Fitbit(consumer_key, consumer_secret, user_key=user_key, user_secret=user_secret)

max_step_stats = authd_client.time_series('activities/steps',user_id=uid,end_date=end_date,base_date='today')
stepsjson = json.loads(json.dumps(max_step_stats))

for key,value in stepsjson.iteritems():
	for date in value:
		day = date.get('dateTime')
		jsonfile = jsondir + day + ".json"
		if not os.path.isfile(jsonfile) and day != today:
			file = open(jsonfile,'w+')
			json.dump(date,file)
			file.close()

