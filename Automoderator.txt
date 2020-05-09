# ================================================================================================================================= #
# ================================== r / S G E X A M S   A U T O M O D E R A T O R   C O N F I G ================================== #
# ===================================================== v e r s i o n   6 . 0 ===================================================== #
#                                                                    •                                                              #  
# =========================== u p d a t e d   1 0   O C T   2 0 1 9   b y   R A N D O M Y S T I C K =========================== #
# ================================================================================================================================= #
# ======= C O N T E N T S ========
# = META: ========================
# === Welcome Message
# === Title Tag Checker
# === Auto Post Flairing 
# = TRIGGERS: ====================
# === Group Chats
# === Vulgarity Check
# === Exams.sg
# === Mental Health
# = ANTI-SPAM: ===================
# === Mass Report Finder
# === External Link Filter
# = LEGACY COMMANDS: =============
# === !remove Command
# === New Account Restrictor
# = Appendix A: DOCUMENTATION
# ================================



# ================================================================================================================================
# ============================================================= META =============================================================
# ================================================================================================================================
---
# WELCOME TO R/SGEXAMS PRIVATE MESSAGE #
    type: submission
    is_edited: false
    message: |
        Hey /u/{{author}}! (⌒∇⌒) Thanks for your submission to r/SGExams regarding {{title}}. While you wait for your post to fill, here are some things you can do in the meantime:



         • **Check out the pinned megathread at the top of r/SGExams!**

            ➥ These are excellent for general comments where a detailed reply isn't needed, and serves as a common place for relevant parties to mingle.



         • **Search r/SGExams for past threads on the matter!**

            ➥ We've been around for quite a while now, so your question might already have been answered previously.



         • **Browse the rest of r/SGExams to help out your fellow peers/juniors!**

            ➥ SGExams wouldn't be what it is today without your continued support and our pay-it-forward culture, and we hope you'll stick around to answer questions on other threads!


        *Have trouble getting your post onto r/SGExams? Read our troubleshooting guide [here](https://www.reddit.com/r/SGExams/comments/bp7pe3/meta_posts_not_getting_through_read_me_sgexams/).*


        Once again, we wish to extend a warm welcome to you, whether you're a new user posting for the very first time or a regular checking in with the community ⊂(・ヮ・⊂). 


        We hope you'll continue being a part of our shared r/SGExams story, and wish you a good time! \\(\^■\^)/

    message_subject: "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧  Welcome to r/SGExams!  ✧ﾟ･: *ヽ(◕ヮ◕ヽ)"


# ================================================================================================================================

---
# Title Tag Requirements - Rule #1 Enforcer #
    ~title: [
      "[N-Levels]","[N-Level]","[N Levels]","[N Level]",
      "[O-Levels]","[O-Level]","[O Levels]","[O Level]",
      "[A-Levels]","[A-Level]","[A Levels]","[A Level]",
      "[University]","[Uni]",
      "[Post-Exams]","[Post-Exam]","[Post Exams]","[Post Exam]",
      "[META]",

      "[Poly]","[Polytechnic]",
      "[IB Diploma]","[IB]",
      "[ITE]","[Institute of Technical Education]",

      "[Scholarships]","[Scholarship]",
      "[Olympiads]","[Olympiad]","[OLYMPIADS]","[OLYMPIAD]",

      "[BMAT]","[SAT]",


]
    comment: |
        Your post has been automatically removed because you did not include one of the required title tags.

        Please read the subreddit post submission rules (Rule #1) for more information.
    action: remove


# ================================================================================================================================

---
# Auto-Flairing of Posts and User #

title: [
    "[N-Levels]","[N-Level]","[N Levels]","[N Level]"
]
set_flair:
    template_id: 78c18084-d82a-11e9-b397-0ebe248adef6
author: 
   set_flair:  
      template_id: 02ec3a0a-07a8-11e9-a7e6-0e41003b1ad6
   overwrite_flair: false

---
title: [ 
    "[O-Levels]","[O-Level]","[O Levels]","[O Level]" 
]
set_flair:
    template_id: 1cf20642-07a7-11e9-8fb7-0e0d65a9aed0
author: 
   set_flair:  
      template_id: 02ec3a0a-07a8-11e9-a7e6-0e41003b1ad6
   overwrite_flair: false

---
title: [
    "[A-Levels]","[A-Level]","[A Levels]","[A Level]"
]
set_flair:
    template_id: 2d6f9dfe-07a7-11e9-8f3b-0e0ac9761a4a
author: 
   set_flair:  
      template_id: 0b820fd2-07a8-11e9-8c13-0eb607f17e34
   overwrite_flair: false

---
title: [
    "[University]","[Uni]"
]
set_flair:
    template_id: 4ee86f06-07a7-11e9-90b3-0e8975bb3ebe
author: 
   set_flair:  
      template_id: 15dfaa7a-07a8-11e9-b025-0e8c76bbd30a
   overwrite_flair: false

---
title: [
    "[Poly]","[Polytechnic]"
]
set_flair:
    template_id: 2411c4ae-0c33-11e9-a449-0ecdab80ffea
author: 
   set_flair:  
      template_id: 1e4f2436-0c5a-11e9-b115-0eb25bd7c020
   overwrite_flair: false

---
#XP: Auto flair ITE
title (regex): ['(ITE|Institute of Technical Education)']
type: submission
set_flair:
    template_id: 724ea874-e5a6-11e9-98d5-0eaa367eb40e
author: 
   set_flair:  
      template_id: ff22dc58-e5a5-11e9-8f4e-0eb08bc17452
   overwrite_flair: false


---
title: [
    "[Post-Exams]","[Post-Exam]","[Post Exams]","[Post Exam]"
]
set_flair:
    template_id: 8b24697a-07a7-11e9-b973-0ee7cc9723b4

---
title: [
    "[META]"
]
set_flair:
    template_id: a05c271a-07a7-11e9-bfda-0e7e029ca2aa

---
title: [
    "[IB Diploma]","[IB]"
]
set_flair:
    template_id: 48408d6a-0c33-11e9-83be-0e73afc8ce4a

---
title: [
    "[Scholarships]","[Scholarship]",
]
set_flair:
    template_id: c8d742c6-0c32-11e9-b66a-0ee4066cbe44

---
title: [
    "[Olympiads]","[Olympiad]","[OLYMPIADS]","[OLYMPIAD]",
]
set_flair:
    template_id: 01e89dbc-0c33-11e9-80d5-0eb91cdc0050

---
title: [
    "[BMAT]","[SAT]"
]
set_flair:
    template_id: e2bec34e-0c32-11e9-83ed-0e0d65a9aed0



# ================================================================================================================================
# =========================================================== TRIGGERS ===========================================================
# ================================================================================================================================
---
# Whatsapp/Telegram/Discord/WeChat Groups (for TITLES) #
    title: [
      "telegram", "tele",
      "whatsapp", "whatsap",
      "discord",
      "wechat",
]
    is_edited: false
    comment: |
        r/SGExams has its very own **[Discord](https://discord.gg/c5wEHZz)** and **[Telegram](https://t.me/SGExamsStudies)** chat/study groups for you to interact with fellow SGExams peeps and/or get and give homework help!

        Feel free to join other community-created chat groups if you wish, but do stay safe and exercise discretion as *online interactions outside of the official SGExams Subreddit, Discord and Telegram platforms are not monitored by us.* Joining a WhatsApp group will also compromise your phone number.

        > \>> **Read more @ [A Note on Group Chats - SGExams](https://www.reddit.com/r/SGExams/comments/b3tzzz/a_note_on_group_chats_sgexams/)** <<

        Cheers and stay safe!


# ================================================================================================================================

---
# Whatsapp/Telegram/Discord/WeChat Groups (for COMMENTS) #
    body: [
      "telegram", "tele",
      "whatsapp", "whatsap",
      "discord",
      "wechat",
]
    is_edited: false
    comment: |
        r/SGExams has its very own **[Discord](https://discord.gg/c5wEHZz)** and **[Telegram](https://t.me/SGExamsStudies)** chat/study groups for you to interact with fellow SGExams peeps and/or get and give homework help!

        Feel free to join other community-created chat groups if you wish, but do stay safe and exercise discretion as *online interactions outside of the official SGExams Subreddit, Discord and Telegram platforms are not monitored by us.* Joining a WhatsApp group will also compromise your phone number.

        > \>> **Read more @ [A Note on Group Chats - SGExams](https://www.reddit.com/r/SGExams/comments/b3tzzz/a_note_on_group_chats_sgexams/)** <<

        Cheers and stay safe!


# ================================================================================================================================

---
# Vulgarity Filter (for TITLES) - Rule #2 & #4 Enforcer #
    title: [
      "fuck you", fuckers,
      kys, "kill yourself", 
      knn, ccb, cb, jibai, ji bai, chaojibai, "chao jibai", "chao ji bai", lanjiao
]
    message: |
        Your post has been automatically flagged for containing inappropriate phrases and will be reviewed manually by a moderator for hurtful or inflammatory content. Please read the subreddit rules (Rule #2) for more information.

        If this is a false flag, you can safely ignore this message. 
    action: report
    action_reason: Automated Vulgarity Filter

---
# Vulgarity Filter (for COMMENTS) - Rule #2 & #4 Enforcer #
    body: [
      "fuck you", fuckers,
      kys, "kill yourself", 
      knn, ccb, cb, jibai, ji bai, chaojibai, "chao jibai", chao ji bai, lanjiao
]
    comment: |
        Your post has been automatically flagged for containing inappropriate phrases and will be reviewed manually by a moderator for hurtful or inflammatory content. Please read the subreddit rules (Rule #2) for more information.

        If this is a false flag, you can safely ignore this message. 
    action: report
    action_reason: Automated Vulgarity Filter


# ================================================================================================================================

---
# Exams.sg Plug (for COMMENTS) #
    body: [
      "study resources", "study material", "study materials", "revision material"
]
    is_edited: false
    comment: |
        SGExams has a [whole library](https://exams.sg/library) of study resources and notes for your mugging endeavours! From national exams (O/A levels) to IB, there's something for every subject and we're still growing our library! Check it out @ https://exams.sg/library. Cheers!


# ================================================================================================================================

---
# Mental Health Warning (for TITLES) #
    title: [
      depression, depressed, depressing
      anxiety, hurt, pain, self-harm, "cut myself"
] 
    action: report
    action_reason: Mental Health Warning

---
# Mental Health Warning (for COMMENTS) #
    body: [
      depression, depressed, depressing
      anxiety, hurt, pain, self-harm, "cut myself"
] 
    action: report
    action_reason: Mental Health Warning


# ================================================================================================================================

#---
# XP, Rando
#type: comment
#body (regex): ['.*']
#parent_submission:
#    flair_template_id: 2af16b32-a2fe-11e9-b6ba-0e150755ddf4
#    comment: |
#        Welcome to the Exam Megathread for today's {{title}}! To view the most recent comments, tap the __"Best Comments"__ option on the top left and select __"New Comments"__ from the dropdown. Thanks! 
#    comment_stickied: true

---
# XP: Auto sort megathread comments by New (2)
type: comment
body (regex): ['.*']
parent_submission:
    flair_template_id: 2af16b32-a2fe-11e9-b6ba-0e150755ddf4
    set_suggested_sort: best


# ================================================================================================================================
# ========================================================== ANTI-SPAM ===========================================================
# ================================================================================================================================
---
# AutoModerator Report Responses (1/2) #
    reports: 3
    modmail: The above {{kind}} by /u/{{author}} has received 3 reports. Please investigate.

---
# AutoModerator Report Responses (1/2) #
    reports: 5
    modmail: The above {{kind}} by /u/{{author}} was removed because it received 5 reports. Please investigate and ensure that this action was correct.
    action: remove


# ================================================================================================================================

---
# Filters External Links #
    type: text submission
    body (regex, full-text): '(\[.*?\]\()?https?://\S+\)?'
    action: filter


# ================================================================================================================================
# ==================================================== LEGACY/DEFUNCT CONFIGS ====================================================
# ================================================================================================================================
#
#---
# !remove Command Attempt #
# Removal Reason: Automod removes the !remove comment instead of the post or comment it is on. Reddit limitation. Correct as at 101019. #
# https://www.reddit.com/r/AutoModerator/comments/b47btq/make_the_automod_comment_the_parent_submission/ #
#moderators_exempt: false
#type: comment
#body: "!remove"
#author:
#  is_moderator: true
#parent_submission
#   action: remove
#   comment: |
#       This post has been removed for violating a rule.
#
#---
# New Account Restrictions === REMOVED 10 MARCH 2019. #
#    author:
#        account_age: < 1 day
#        combined_karma: < -1
#        satisfy_any_threshold: true
#        is_contributor: false
#    ~author: [Randomystick, jaydxn1] #whitelist, not usually needed (individual approvals will do)
#    message: |
#        Your post has been automatically removed because you do not meet the criteria to post here. Your reddit account must be at least 1 day old #and have > -1 karma. Otherwise, your submissions will be automatically deleted by the AutoModerator to prevent spamming and to protect the quality #of content posted here. You can message the moderators via modmail to have your content approved and/or your account whitelisted if you don't want #to wait for your reddit account to reach 1 day old.
#    action: remove
#
# ================================================================================================================================



# ================================================================================================================================
# ========================================================= DOCUMENTATION ========================================================
# ================================================================================================================================

# Hello there! It looks like you may be asking about how to require users to set linkflair on their posts.
# AutoModerator is not able to do this. AutoModerator evaluates content as it's being posted. Since linkflair cannot be set until after a submission is already posted, submissions will never have linkflair when AutoModerator is looking at it.
# Additionally, AutoModerator is not able to review content after time has passed. AutoModerator can only evaluate something when it's created, edited, or reported, and at no other times.
