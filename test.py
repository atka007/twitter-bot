from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

my_bot.sync_follows()
#my_bot.send_tweet("Hello world!")

#my_bot.auto_follow("cars")

#my_bot.auto_follow("CNET")
my_bot.auto_follow_followers_of_user("CNET", count=20)
my_bot.auto_follow_followers_of_user("wired", count=20)
my_bot.auto_follow_followers_of_user("verge", count=20)
#my_bot.auto_fav("phrase", count=1000)

#my_bot.auto_rt("phrase", count=1000)

#my_bot.auto_unfollow_nonfollowers()
#my_bot.auto_unfollow_all_followers()
