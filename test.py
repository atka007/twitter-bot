from TwitterFollowBot import TwitterBot
import time
import random

my_bot = TwitterBot()
wait_time = 5
accounts = 3
daily_followings = 10
actions = daily_followings / accounts


print("Running Bot!")

#my_bot.send_tweet("Hello world!")

#Sync follows every day
#my_bot.sync_follows()

#my_bot.auto_follow("cars")

#my_bot.auto_follow("CNET")

for x in range(6):
  print("Loop: " + str(x))
  time.sleep(wait_time)
  
  #my_bot.auto_follow_followers_of_user("CNET", count=actions)
  
  #my_bot.auto_fav("luxury", count=10)
  
  #my_bot.auto_follow_followers_of_user("wired", count=actions)
  
  #my_bot.auto_follow_followers_of_user("verge", count=actions)
  
  #my_bot.auto_unfollow_all_followers()
  

#my_bot.auto_rt("phrase", count=1000)

#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()


#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("BOT Finished Process!")
