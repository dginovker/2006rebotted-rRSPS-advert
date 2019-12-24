import praw
import time
from random import randint
from time import sleep

reddit = praw.Reddit("2006-REBOTTED", user_agent = 'Thread advertiser by /u/OsrsNeedsF2P')

advertisement = """
# 2006rebotted

The most accurate & authentic 2006 remake. Why? Because 2006 had bots.

### [DISCORD](https://discord.gg/ry2BSP2)

### [RUNE-SERVER ANNOUNCEMENT](https://www.rune-server.ee/runescape-development/rs2-server/advertise/689762-perfecting-one-remake-2006rebotted-open-source-remake-hundreds-updates.html)

### [SOURCE CODE](https://github.com/dginovker/2006rebotted)

## ★★★JOIN THE MOST ACTIVE REMAKE TODAY★★★

### >>>> [PARABOT DOWNLOAD](https://www.parabot.org/community/) <<<<<
"""

def comment_submission(submission):
    sleep(randint(1000,7200))
    submission.reply(advertisement)
    return


def find_submissions():
    try:
        while True:
            start_time = time.time()
            for submission in reddit.subreddit("RSPS").stream.submissions():
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
