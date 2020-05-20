from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

#my_bot.send_tweet("Hello world!")

#Sync follows every day
while True:
  my_bot.sync_follows()
  wait(86400)


#my_bot.auto_follow("cars")

#my_bot.auto_follow("CNET")
my_bot.auto_follow_followers_of_user("CNET", count=100)
my_bot.auto_follow_followers_of_user("wired", count=100)
my_bot.auto_follow_followers_of_user("verge", count=100)
#my_bot.auto_fav("phrase", count=1000)

#my_bot.auto_rt("phrase", count=1000)

my_bot.auto_unfollow_nonfollowers()
my_bot.favorite_following_tweets()
#my_bot.auto_unfollow_all_followers()
