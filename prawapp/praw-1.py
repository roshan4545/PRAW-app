import random
import praw
import config
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     password=config.password,
                     user_agent="trivikram dialogue bot v1.0 by roshan-malipatel",
                     username=config.username)
lines = ["Logic lu evaru nammaru, Andariki magic le kavali, anduke mana desham lo scientists la kante Baba le famous",
"Manushulu puttaake sampradaayalu puttayi, sampradayalu puttaka manushulu puttaledu",
"Nijam cheppetappude bayam vestundi, cheppakapothe eppudu bayamesthundi",
"Sampadinchadam chethakaani vadiki karchu pette arhatha ledu",
"Nenu okariki nachakapothe adhi valla problem, na problem kaadu",
"Amayakula kosam chese yuddam lo amayakulu chanipothe, manam chese yuddaniki ardhamemundi",
"Ekkada neggalo kaadu, ekkada thaggalo thelisinode goppodu",
"Karanam leni kopam, gouravam leni prema, badhyata leni yavvanam, gnapakalu leni vrudhaypyam anavasaram"]
while(True):
    for comment in reddit.subreddit("chernobyl").stream.comments(skip_existing=True):
        comm = str(comment.body)
        print(comm)
        if(comm.find("trivikramdialouge!")!=-1):
            comment.reply(lines[random.randint(0,len(lines)-1)])