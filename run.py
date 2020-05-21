from TwitterFollowBot import TwitterBot
import random
import time
import math

my_bot = TwitterBot()
wait_time = 5
repeat_actions = 30

accounts = 3
max_actions = 3

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
  rnd=random.randint(1,max_actions) 
  my_bot.auto_follow_followers_of_user("CNET", count=rnd)  
  
  #Like something
  my_bot.auto_fav("luxury", count=1)
  
  rnd=random.randint(1,max_actions) 
  my_bot.auto_follow_followers_of_user("wired", count=rnd) 
  
  #Retweet Something
  my_bot.auto_rt("cool", count=1)
  
  rnd=random.randint(1,max_actions) 
  my_bot.auto_follow_followers_of_user("verge", count=rnd)
      
  #Unfolow people
  unfollow_num = accounts * max_actions
  my_bot.auto_unfollow_all_followers(unfollow_num)
  
  
  
  

#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()


#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("BOT Finished Process!")
