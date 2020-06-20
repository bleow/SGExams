import praw #reddit
import xlsxwriter #export to excel
import SGExams_Login


#################################################
################## REDDIT PART ##################
#################################################

# Reddit OAuth Details & Init to SGExams
reddit = praw.Reddit(client_id = SGExams_Login.client_id,
                     client_secret = SGExams_Login.client_secret,
                     username = SGExams_Login.username,
                     password = SGExams_Login.password,
                     user_agent = f"reddit:postwordcounter by {SGExams_Login.username}",
                     )
subreddit = reddit.subreddit("SGExams")

# Obtain top x posts - CHANGE LIMIT IF NEEDED
sgexams_posts = subreddit.new(limit=15) 

# Populate array of arrays postsArray with data
# Note: in Python arrays are called lists
postsArray = []
indexNo = 1
for posts in sgexams_posts:
    upvoteCount = posts.ups
    wordCount = len(posts.selftext.split())
    charCount = len(posts.selftext)
    url = posts.url
    postsArray.append([indexNo, upvoteCount, wordCount, charCount, url])
    indexNo = indexNo +1


################################################
################## EXCEL PART ##################
################################################

# Different excel filenames
test = 'export01.xlsx'
final = 'SGExams_WordCount.xlsx'

# xlsxwriter
workbook = xlsxwriter.Workbook(test)
worksheet = workbook.add_worksheet("sheet1") 

# Custom formatting options
bold = workbook.add_format({'bold': True, 'font_color': '#07d6ea', 'text_wrap': True, 'bg_color': '#2f2f41'})

# Write headers
worksheet.write('A1', 'INDEX NUMBER', bold)
worksheet.write('B1', 'UPVOTE COUNT', bold)
worksheet.write('C1', 'WORD COUNT', bold)
worksheet.write('D1', 'CHAR COUNT', bold)
worksheet.write('E1', 'URL', bold)

# Iterate over the data and write it out row by row. 
row = 1
col = 0
for indexNo, upvoteCount, wordCount, charCount, url in (postsArray):
    worksheet.write(row, col + 0, indexNo)
    worksheet.write(row, col + 1, upvoteCount)
    worksheet.write(row, col + 2, wordCount)
    worksheet.write(row, col + 3, charCount)
    worksheet.write(row, col + 4, url)
    row += 1


# Close excel file
workbook.close() 


'''
for lol in sgexams_posts:
    print(dir (lol)) # print list of commands to use with posts
'''


#################################################
################### FOOTNOTES ###################
#################################################

# Debugging
## No module named 'modulename' -- run 'pip install modulename' in cmd
##                              -- Check the bottom left that the Python version chosen is the latest
## [Errno 13] Permission denied: 'excelfile.xlsx' -- close the excel file
