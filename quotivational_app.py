#Access to the quotes database
from flask import Flask, jsonify, json, request, make_response, ssl
import ssl

#with open('quotes.json') as f:
    #all_motivational_quotes = json.load(f)


all_motivational_quotes = [
	{
		"topic" : "procrastination", 
		"quote_series":[
		    {"quote":"Never put off for tomorrow what you can do today.","author":"Thomas Jefferson"},
		   	{"quote":"Don’t put off for tomorrow what you can do today, because if you enjoy it today, you can do it again tomorrow.","author":"James Michener"},
		   	{"quote":"The greatest amount of wasted time is time not getting started.","author":"Dawson Trotman"},
			{"quote":"Anything worth putting off is worth abandoning altogether.","author":"Epictetus"},
			{"quote":"The least productive people are usually the ones who are most in favor of holding meetings.","author":"Thomas Sowell"},
			{"quote":"Your mind is for having ideas, not holding them.","author":"David Allen"},
			{"quote":"Regret for the things we did can be tempered by time - it is regret for the things we did not do that is inconsolable.","author":"Sydney Harris"},
			{"quote":"Nothing is so fatiguing as the eternal hanging on of an uncompleted task.","author":"William James"},
			{"quote":"Successful people do daily what others do occasionally.","author":"Paula White"},
		],
	},
	
	{
		"topic" : "perfectionism", 
		"quote_series":[
		    {"quote":"The essence of being human is that one does not seek perfection.","author":"George Orwell"},
		   	{"quote":"Perfectionism is a dream killer, because it’s just fear disguised as trying to do your best.","author":"Mastin Kipp"},
		   	{"quote":"There is no perfection, only beautiful versions of brokenness.","author":"Shannon Alder"},
			{"quote":"Embrace being perfectly imperfect - learn from your mistakes and forgive yourself, you’ll be happier.","author":"Roy Bennett"},
		],
	},
	
	{
		"topic" : "stress", 
		"quote_series":[
		    {"quote":"One of the symptoms of an approaching nervous breakdown is the belief that one's work is terribly important.","author":"Bertrand Russell"},
		   	{"quote":"Sometimes the most productive thing you can do is relax.","author":"Mark Black"},
		   	{"quote":"Almost everything will work again if you unplug it for a few minutes… Including you.","author":"Anne Lamott"},
			{"quote":"The key is not to prioritize what’s on your schedule, but to schedule your priorities.","author":"Stephen Covey"},
			{"quote":"You can do anything - but not everything.","author":"David Allen"},
			{"quote":"Stressed spelled backwards is desserts.","author":"Loretta Laroche"},
		],
	},

	{
		"topic" : "revision",
		"quote_series":[
		   	{"quote":"Trust yourself, you know more than you think you do.","author":"Benjamin Spock"},
		   	{"quote":"Don’t let what you cannot do interfere with what you can do.","author":"John Wooden"},
			{"quote":"If you can't explain it simply, you don't understand it well enough.","author":"Albert Einstein"},
			{"quote":"Motivation is what gets you started, habit is what keeps you going.","author":"Jim Ryun"},
			{"quote":"Learning is a treasure that will follow its owner everywhere.","author":"Unknown"},
			{"quote":"The man who does not read books has no advantage over the man who cannot read them.","author":"Mark Twain"},
		],
	},
]

app = Flask(__name__)

#Login, logout, sign up

@app.route("/")
def homepage():
    html = "<h1>Welcome to your Task List!</h1>"
    return html

@app.route("/login")
def login():
	return "<p>Login</p>"

@app.route("/logout")
def logout():
    return "<p>Logout</p>"

@app.route("/sign-up")
def sign_up():
    return "<p>Sign Up</p>"

#GET method to access quotes

@app.route("/motivational_quotes/", methods=['GET'])
def get_motivational_quotes():
		return jsonify(all_motivational_quotes), 200


@app.route("/motivational_quotes/quotes_by_topic/<topicname>/", methods=['GET'])
def get_quotes_by_topic(topicname):
	response={topicname:"Not Found!"}, 404
	for item in all_motivational_quotes:
		if item["topic"]==topicname:
			response = [x["quote"] for x in item["quote_series"]]
			break
    	return jsonify(response), 200

#POST method to create quotes and topics

@app.route("/motivational_quotes", methods=['POST']) 
def create_a_quote():
    if not request.json or not 'topic' in request.json:
        return jsonify({'error':'the new quote needs to have a topic name'}), 400
    new_quote = {'topic': request.json['topic'],
                 'quote_series': request.json.get('quote_series', '')}

    all_motivational_quotes.append(new_quote)
    return jsonify({'message': 'created: /motivational_quotes/{}'.format(new_quote['topic'])}), 201


#curl -i -H "Content-Type: application/json" -X POST -d ’{"topic":[],"quote_series":"Hello"}’ http://35.246.39.23:8880/motivational_quotes



#DELETE method to delete topics

@app.route('/motivational_quotes/quotes_by_topic/<topicname>', methods=['DELETE']) 
def delete_a_topic(topicname):
  matching_topic = [x for x in all_motivational_quotes if x['topic'] == topicname] 
  if len(matching_topic)==0:
    return jsonify({'error':'topic name not found!'}), 404 
  all_motivational_quotes.remove(matching_topic[0])
  return jsonify({'success': True})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 80, ssl_context=context)

#api random advice

from flask import render_template
import json
import requests
import requests_cache

app = Flask (__name__)

advice_url_template = "https://api.adviceslip.com/advice"

@app.route('/randomadvice', methods=['GET'])
def get_advice():
  resp = requests.get(advice_url_template)
  if resp.ok:
    return jsonify(resp.json())
  else: 
    print(resp.reason)
  
if __name__=='__main__':
  app.run(host='0.0.0.0')


#new code for authentication

from flask import Flask, request, make_response
from functools import wraps

app = Flask(__name__)

@app.route('/au')

def index():
  if request.authorization and request.authorization.username == 'group1' and request.authorization.password == 'pass1234':
    return '<h1>You are logged in </h1>'
  
  return make_response('Could not verify user, please check your username and password!', 401)

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 80)


