# SGExams
Written for managing the r/SGExams subreddit, using Python Reddit API Wrapper (PRAW). Languages: Python || Date created: Apr 2019

## Python Libraries
- Ensure you have the relevant libraries installed in your computer. PRAW is a must, other libraries are program specific.
- They can be installed by going into command prompt and typing "pip install _____"

## SGExams_Login
- This is the config file used to authenticate with Reddit's API where you provide your Reddit account details. The file in this repo is a dummy (I removed my own login details, obviously) so remember to supply your own credentials. Some scripts may require a mod account to execute.


## Debugging
Problem: ModuleNotFoundError: No module named 'praw'
Solution 1: run pip install (see Python Libraries section)
Solution 2: If running in an IDE, check that the version number your IDE is running in (in Visual Studio Code, available in the bottom left on the blue header) is the same as the latest version you have installed on your computer. To do so,
1. Run import sys and print(f"{sys.date}") in VSCode
2. Run import sys and sys.date in command prompt
3. If the directories returned by the above two are mismatched, change the VSCode version to the cmd version
