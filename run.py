from TwitterFollowBot import TwitterBot
from random import random
import time
import math

my_bot = TwitterBot()
wait_time = 5
repeat_actions = 30

accounts = 3
daily_followings = 7
#act = int(daily_followings / accounts)

print("Running Bot!")

#my_bot.send_tweet("Hello world!")

#Sync follows every day
my_bot.sync_follows()

#my_bot.auto_follow("CNET")

for x in range(repeat_actions):
  print("Loop: " + str(x))

  #Random Wait Up to 5 min
  #time.sleep(random() * 5 * 60)

  #print("Act: " + str(act))

  #Follow people
  my_bot.auto_follow_followers_of_user("CNET", count=2)  
  
  #Like something
  my_bot.auto_fav("luxury", count=1)
  
  my_bot.auto_follow_followers_of_user("wired", count=2) 
  
  #Retweet Something
  my_bot.auto_rt("cool", count=1)
  
  my_bot.auto_follow_followers_of_user("verge", count=2)
      
  #Unfolow people
  #my_bot.auto_unfollow_all_followers(2)
  
  
  
  

#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()


#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("BOT Finished Process!")
