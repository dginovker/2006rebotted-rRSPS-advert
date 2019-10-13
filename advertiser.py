import praw
import time

reddit = praw.Reddit("2006-REBOTTED", user_agent = 'Thread advertiser by /u/OsrsNeedsF2P')

advertisement = """
# 2006rebotted

The most accurate & authentic 2006 remake. Why? Because 2006 had bots.

### [DISCORD](https://discord.gg/ry2BSP2)

### [RUNESUITE ANNOUNCEMENT](https://runesuite.org/rsps-forum/forums/topic/4487-2006rebotted-open-source-bug-fixed-remake-based-on-2006redone-constant-updates/)

### [SOURCE CODE](https://github.com/dginovker/2006rebotted)

## ★★★JOIN THE MOST ACTIVE REMAKE TODAY★★★

### >>>> [PARABOT DOWNLOAD](https://www.parabot.org/community/) <<<<<
"""

def comment_submission(submission):
    submission.reply(advertisement)
    return


def find_submissions():
    try:
        while True:
            start_time = time.time()
            for submission in reddit.subreddit("Monero").stream.submissions():
                if submission.created_utc > start_time and "weekly" in submission.title.lower() and submission.author.name.lower() == "automoderator":
                    comment_submission(submission)
                    break
    except Exception as e:
        print("Exception caught: ")
        print(e)
        find_submissions()

if __name__ == '__main__':
    print("Starting 2006rebotted advertiser..")
    find_submissions()
