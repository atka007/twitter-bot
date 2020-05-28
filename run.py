from TwitterFollowBot import TwitterBot
import random
import time
import math

my_bot = TwitterBot()

#Lists
reTweetSourceList = ["11hr11min","mashable","wired","cnet","EducationalPic","EmojiMashupPlus","Lifehacker","engadget",
                     "verge","thenextweb","digitaltrends","roadshow","themotleyfool","hypebeast","DIYDrones","BritishGQ",
                     "LouboutinWorld","univercurious","kicksonfire","theDIYhacks","omglifehacks"]
likeSourceList = ["luxury","mashable","wired","cnet"]

#Timers
wait_time = 0.25  #minutes
repeat_actions = 300
likes = 1
retweets = 1
accounts = 3
max_actions = 3

#Controls
cntrl_follow = 0
cntrl_unfollow = 0
cntrl_retweet = 1
cntrl_like = 0

daily_actions = repeat_actions * ((accounts * max_actions) + likes + retweets)
print("Daily Actions: " + str(daily_actions))

print("Running Bot!")
#my_bot.send_tweet("Hello world!")

#Sync follows every day
my_bot.sync_follows()

#Follow
def do_follow(self):
  if cntrl_follow == 1:
    rnd=random.randint(1,max_actions) 
    my_bot.auto_follow_followers_of_user("CNET", count=rnd)  
    
#Unfolow
def do_unfollow(self):
  if cntrl_unfollow == 1:
    unfollow_num = accounts * max_actions
    my_bot.auto_unfollow_all_followers(unfollow_num)

#Retweet
def do_retweet(self):
  if cntrl_retweet == 1:
    try:
      rndTweet=random.randint(0,len(reTweetSourceList)-1)
      print("rndTweet: " + str(rndTweet))
      reTweetSource=reTweetSourceList[rndTweet]
      print("reTweetSource: " + str(reTweetSource))   
      my_bot.auto_rt(reTweetSource, count=retweets)
    except:
      print("This didn't work for some reason!")  
 
#Like
def do_like(self):
  if cntrl_like == 1:
    try:
      rndLike=random.randint(0,len(likeSourceList)-1)
      print("rndLike: " + str(rndLike))
      likeSource=likeSourceList[rndLike]
      print("likeSource: " + str(likeSource))
      my_bot.auto_fav(likeSource, count=likes)
    except:
      print("This didn't work for some reason!")  


for x in range(repeat_actions):
  print("Loop Number: " + str(x))

  option = random.randint(0, 4)
  if option == 0:
    print("do_follow")    
  elif option == 1:
    print("do_unfollow") 
  elif option == 2:
    print("do_retweet") 
  elif option == 3:
    print("do_like") 
  else:
    print("do_message") 
 
  #Random Wait
  time.sleep(random() * wait_time * 60)
    
    
#my_bot.auto_follow("CNET")    
#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()

#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("BOT Finished Process!")
