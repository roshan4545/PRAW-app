# PRAW-app

There are lots of restrictions on Reddit Bots, so read the Reddit Bottiquete when planning your project. Essentially, make sure your bot is useful, and does not spam or comment when it is not invoked.

To prevent your bot from being banned, allow it to only function in specific subreddits. Lots of times, bots are banned because they are spamming communities or are being invoked out-of-context. Limiting functionality to certain communities can prevent this from happening.

Reddit bots are registered as 'scripts' running under a Reddit user account. So, when setting up your config.py file, first create a new Reddit account, and use those credentials. Also, remember not to share or upload the config.py file on Github!

We can also pushshift.io, that allows you to search all of Reddit. Use the after keyword in the query to find results from after the last time the bot was invoked so the query runs quickly!But here i have used praw from python and you can makesome changes in code to use the pushshift.io api.

we can automate the bot using docker in combination with Azure ACI for bot to run continuously.

How to use this bot

As of now, it works only on the r/chernobyl (i have just taken it as the sample subreddit and you can use any subreddit of your choice) and it works when any user has commented "trivikramdialouge!" on any post of that particular subreddit and it will randomly comment any trivikram dialouge from a set of dialouges which are in the praw-1.py file and we can make some change and use this to perform any action of our choice.
