import praw #reddit
import SGExams_Login

reddit = praw.Reddit(client_id = SGExams_Login.client_id,
                     client_secret = SGExams_Login.client_secret,
                     username = SGExams_Login.username,
                     password = SGExams_Login.password,
                     user_agent = "reddit:flairchanger by rando",
                     )
subreddit = reddit.subreddit("SGExams")

#FLAIRS
plant2020b = 'a0b11648-71a1-11ea-b345-0ebee32aa3e1'
plant2020special = 'bbc5a4da-7aa7-11ea-a222-0eda625f8381'

for users in 
user = r.get_redditor('REDDITOR-USER-HANDLE')


#flair_mapping = [{'user':'bboe', 'flair_text':'dev'}, {'user':'pyapitestuser3', 'flair_css_class':'css2'}, {'user':'pyapitestuser2', 'flair_text':'AWESOME', 'flair_css_class':'css'}] 
#r.get_subreddit('python').set_flair_csv(flair_mapping) ```

























"""
# https://alpscode.com/blog/how-to-use-reddit-api/

# REQUEST ACCESS TOKEN
import SGExams_Login
import requests
base_url = 'https://www.reddit.com/'
data = {'grant_type': 'password', 'username': SGExams_Login.username, 'password': SGExams_Login.password}
auth = requests.auth.HTTPBasicAuth(SGExams_Login.client_id, SGExams_Login.client_secret)
r = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'test by RANDO'},
		  auth=auth)
d = r.json()
#print(f"{d}")


# API REQUESTS TO OAUTH.REDDIT NOT REDDIT
token = 'bearer ' + d['access_token']
base_url = 'https://oauth.reddit.com'
headers = {'Authorization': token, 'User-Agent': 'test by RANDO'}
response = requests.get(base_url + '/api/v1/me', headers=headers)
#if response.status_code == 200:
#    print(response.json()['name'], response.json()['comment_karma'])


payload = {'q': 'puppies', 'limit': 5, 'sort': 'relevance'}
response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
print(response.status_code)
"""