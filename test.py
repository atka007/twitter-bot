from TwitterFollowBot import TwitterBot
import time
import random

my_bot = TwitterBot()
wait_time = 60
print("Running Bot!")
#my_bot.send_tweet("Hello world!")

#Sync follows every day
#my_bot.sync_follows()

#my_bot.auto_follow("cars")

#my_bot.auto_follow("CNET")

for x in range(6):
  print(x)
  time.sleep(wait_time)
  #my_bot.auto_follow_followers_of_user("CNET", count=100)
  #my_bot.auto_follow_followers_of_user("wired", count=100)
  #my_bot.auto_follow_followers_of_user("verge", count=100)
#my_bot.auto_fav("phrase", count=1000)

#my_bot.auto_rt("phrase", count=1000)

#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()
#my_bot.auto_unfollow_all_followers()


#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("BOT Finished Process!")
