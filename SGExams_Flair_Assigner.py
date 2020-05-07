import praw #reddit
from csv import DictReader #namelist
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

with open(r'C:\Users\Bryan Leow\Documents\Visual Studio 2017\python\namelist.csv', 'r') as read_obj: 
# first r: convert normal string to raw string (if not directory will generate some unicode error); second r: read-only
# Note: Change the directory and filename accordingly on your own system
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        username = reddit.redditor(row['Name'])
        subreddit.flair.set(username, flair_template_id=plant2020special)

