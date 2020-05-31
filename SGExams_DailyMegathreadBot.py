# Max number of days a comment will be carried forward
TIMEOUT = 3

import praw #reddit
import SGExams_Login
import datetime #get today and yesterday
import re  #regex search for "ｐｏｓｔｅｄ  ｂｙ："

# Reddit OAuth Details & Init to SGExams
reddit = praw.Reddit(client_id = SGExams_Login.client_id,
                     client_secret = SGExams_Login.client_secret,
                     username = SGExams_Login.username,
                     password = SGExams_Login.password,
                     user_agent = f"reddit:sgexamsbot by Randomystick",
                     )
subreddit = reddit.subreddit("SGExamsBETA")

# Format them the same way as configured in the automoderator schedule
today =  datetime.date.today().strftime("%B %d, %Y")
yesterday = (datetime.date.today() - datetime.timedelta(days = 1)).strftime("%B %d, %Y")
# DEBUG # print(f"{today}, {yesterday}")


# RETRIEVE YESTERDAY'S POST
for YSTDpost in subreddit.search(f"Daily Megathread {yesterday}"):
    YSTDsubmission = reddit.submission(url=YSTDpost.url)
# DEBUG # print(f"yesterday post is {YSTDsubmission}")


# "botStamp": details poster's username and date of posting. Appended to the front of every comment (that doesn't already have it)
botStamp = '\*\*ｐｏｓｔｅｄ  ｂｙ：\*\* u/'
# The \ is to escape the *, which in Regex actually means ZERO OR MORE of the previous character

# Initialise list (array) to iterate through and store unreplied comments
unrepliedComments = []


# Simulate clicking "Load more comments" up to 32 times
YSTDsubmission.comments.replace_more(limit=32)

for top_level_comment in YSTDsubmission.comments:
    # For top-level comments with no replies:
    if not (top_level_comment.replies):

        # If comment already has botStamp...
        if re.search(botStamp, top_level_comment.body):
            # ...and date of posting is less than TIMEOUT days ago...
            dateRegex = re.search('\*\*\w+\s\d+,\s20\d{2}\*\*', top_level_comment.body)
            if dateRegex is not None:
                date = dateRegex.group(0).replace('**', '')
            # (no, datetime.datetime is not a typo)
            diff = datetime.datetime.strptime(today, "%B %d, %Y") - datetime.datetime.strptime(date, "%B %d, %Y")
            if (abs(diff.days) < TIMEOUT):
                # ... add it to the list.
                unrepliedComments.append(top_level_comment.body)

        # Else, add the botStampnoEscape
        else:
            # New string has to be created because strings in Python are immutable and replace() returns a string, not modifies the original
            botStampnoEscape = botStamp.replace('\\', '')
            comment = botStampnoEscape + str(top_level_comment.author) + " on " + "**"+yesterday+"**" + " *(Be sure to mention OP in your reply!)*" + "\n\n>" + top_level_comment.body
            unrepliedComments.append(comment)
# DEBUG # for i in unrepliedComments:    print(f"{i}")


# RETRIEVE TODAY'S POST
for TDAYpost in subreddit.search(f"Daily Megathread {today}"):
    TDAYsubmission = reddit.submission(url=TDAYpost.url)
# DEBUG # print(f"today post is {TDAYsubmission.title}")
for i in unrepliedComments:
    TDAYsubmission.reply(f"{i}")
YSTDcomment = TDAYsubmission.reply(f"Go [here]({YSTDsubmission.url}) for yesterday's megathread!")
YSTDcomment.mod.distinguish(sticky=True)


# RETURN STATUS
print("REPOST COMPLETE!")
print(f"POSTED ON: {TDAYsubmission.title}")
print(f"COUNT: {len(unrepliedComments)}")
print("COMMENT LIST:")
for i in unrepliedComments:
    print(f"{i}")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' DEBUGGING 
1) TypeError: list indices must be integers or slices, not str
-- PROB: Writing "for i in unrepliedComments:    print(f"{unrepliedComments[i]}")"
-- SOLN: Write "for i in unrepliedComments:  print(f"{i}")". 
-- NOTE: i already refers to the iterative individual elements in the array, not a counter

DEBUGGING '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
