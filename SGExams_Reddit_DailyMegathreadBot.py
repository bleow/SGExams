''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' CHANGELOG
10-JUN-2020
- Fixed a bug where the bot will comment on the wrong post
  > Added a check for post author == Automoderator when searching for megathread post

CHANGELOG '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' DEBUGGING
Script suddenly stopped working? Here's some mistake-prone areas you may want to check:
1) Servertime-localtime Discrepancy: UTC vs SGT? (line 38)
2) Subreddit Search Terms: sometimes "Daily Megathread {date}" doesn't work in the API even if it does on the
   manual Reddit client. /shrugs/ Play around with the search terms. (lines 44, 87)
3) Regex Date: edge-case that doesn't get recognised by the Regex? (line 68)

DEBUGGING '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# Max number of times a comment will be reposted
TIMEOUT = 3

import praw #reddit
import datetime #get today and yesterday
import re  #regex search for "ｐｏｓｔｅｄ  ｂｙ："

#################################################
################## REDDIT PART ##################
#################################################

# Reddit OAuth Details & Init to SGExams
# USE SGEXAMSBOT NOT YOUR PERSONAL ACCOUNT
reddit = praw.Reddit(client_id = SGExams_Login.client_id,
                     client_secret = SGExams_Login.client_secret,
                     username = SGExams_Login.username,
                     password = SGExams_Login.password,
                     user_agent = f"reddit:sgexamsbot by Randomystick",
                     )
subreddit = reddit.subreddit("SGExamsBETA")

# Format the dates the same way as configured in the automoderator schedule
# NOTE: Because the bot has to run by 6:30AM Singapore time,
####### but the PythonAnywhere server is running on UTC time,
####### when this script runs, it's still the previous day in server time. (22:30 UTC)
####### Therefore, datetime's today() is "today" in UTC time, and yesterday in SGT time.
####### Solution? Make yesterday = "today", and today = "tomorrow".
yesterday =  datetime.date.today().strftime("%B %d, %Y")
today = (datetime.date.today() + datetime.timedelta(days = 1)).strftime("%B %d, %Y")
# DEBUG # print(f"{today}, {yesterday}")


# RETRIEVE YESTERDAY'S POST
for YSTDpost in subreddit.search(f"Daily {yesterday}"):
    if YSTDpost.author == "Automoderator":
        YSTDsubmission = reddit.submission(url=YSTDpost.url)
# DEBUG # print(f"post is {YSTDpost.title}") print(f"yesterday post is {YSTDsubmission.title}")


# "botStamp": details poster's username and date of posting. Appended to the front of every comment (that doesn't already have it)
botStamp = '\*\*ｐｏｓｔｅｄ  ｂｙ：\*\* u/'
# The \ is to escape the *, which in Regex actually means ZERO OR MORE of the previous character

# Initialise list (array) to iterate through and store unreplied comments
unrepliedComments = []


# Simulate clicking "Load more comments" up to 32 times
YSTDsubmission.comments.replace_more(limit=32)

for top_level_comment in YSTDsubmission.comments:
    # For top-level comments with no replies:
    if not (top_level_comment.replies) and not (top_level_comment.stickied):
        # DEBUG # print(f"comment is {top_level_comment.body}")
        # If comment already has botStamp...and date of posting is less than TIMEOUT+1 days ago...
        if re.search(botStamp, top_level_comment.body):
            dateRegex = re.search('\*\*\w+\s\d+,\s20\d{2}\*\*', top_level_comment.body)
            # "if x is not None" is required else .group(0) will throw an error when called because it doesn't exist
            if dateRegex is not None:    date = dateRegex.group(0).replace('**', '')
            # (no, datetime.datetime is not a typo)
            diff = datetime.datetime.strptime(today, "%B %d, %Y") - datetime.datetime.strptime(date, "%B %d, %Y")
            if (abs(diff.days) < (TIMEOUT+1)):
                # ... add it to the list.
                unrepliedComments.append(top_level_comment.body)

        # Else, add the botStampnoEscape
        else:
            # New string has to be created because strings in Python are immutable and replace() returns a string, not modifies the original
            botStampnoEscape = botStamp.replace('\\', '')
            comment = botStampnoEscape + str(top_level_comment.author) + " on " + "**"+yesterday+"**" + " *(Be sure to mention OP in your reply!)*" + "\n\n>" + top_level_comment.body
            # and add it to the list.
            unrepliedComments.append(comment)
# DEBUG # for i in unrepliedComments:    print(f"{i}")


# RETRIEVE TODAY'S POST
for TDAYpost in subreddit.search(f"Daily {today}"):
    if TDAYpost.author == "Automoderator":
        TDAYsubmission = reddit.submission(url=TDAYpost.url)
# DEBUG # print(f"search is Daily {today}") print(f"post are {TDAYpost.title}") print(f"today post is {TDAYsubmission.title}")



# WHERE ALL THE POSTING HAPPENS (COMMENT TO DISABLE)
for i in unrepliedComments:
    TDAYsubmission.reply(f"{i}")
YSTDcomment = TDAYsubmission.reply(f"Go [here]({YSTDsubmission.url}) for yesterday's megathread! 10-JUN-2020: Fixed a bug where the bot will comment on the wrong post. Apologies for the double mention for the users affected! -- u/Randomystick")
YSTDcomment.mod.distinguish(sticky=True)


# RETURN STATUS
print("REPOST COMPLETE!")
print(f"POSTED ON: {TDAYsubmission.title}")
print(f"COUNT: {len(unrepliedComments)}")
print("COMMENT LIST:")
for i in unrepliedComments:
    print(f"{i}")

