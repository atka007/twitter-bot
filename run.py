from TwitterFollowBot import TwitterBot
import random
import time
import math

my_bot = TwitterBot()

#Lists
reTweetSourceList = ["11hr11min","mashable","wired","cnet","EducationalPic","EmojiMashupPlus","Lifehacker","engadget",
                     "verge","thenextweb","digitaltrends","roadshow","themotleyfool","hypebeast","DIYDrones","BritishGQ",
                     "LouboutinWorld","univercurious","kicksonfire","theDIYhacks","omglifehacks"]
likeSourceList = ["luxury","mashable","wired","cnet","EmojiMashupPlus","Lifehacker","11hr11min","luxurywatches","kotaku",
                  "lamborghini","delorean","luxuryvacation"]

greetingList = ['Hey', 'Hi', 'Hello']
messageList = ["please follow us @feed_gift !","you must check us out @feed_gift !","have you heard of www.gift-feed.com? Please follow us @feed_gift to learn more!"]

#Timers
wait_time = 4
repeat_actions = 30
likes = 1
retweets = 1
accounts = 3
max_actions = 3

#Controls
cntrl_follow = 0
cntrl_unfollow = 0
cntrl_retweet = 0
cntrl_like = 1
cntrl_message = 1

daily_actions = repeat_actions * ((accounts * max_actions) + likes + retweets)
print("Daily Actions: " + str(daily_actions))

print("Running Bot!")
#my_bot.send_tweet("Hello world!")

#Sync follows every day
my_bot.sync_follows()

#Follow
def do_follow():
  if cntrl_follow == 1:
    rnd=random.randint(1,max_actions) 
    
    rndFollow=random.randint(0,len(reTweetSourceList)-1)
    print("rndFollow: " + str(rndFollow))
    followSource=reTweetSourceList[rndFollow]
    print("followSource: " + str(followSource))   
        
    my_bot.auto_follow_followers_of_user(followSource, count=rnd) 
    
#DM
def do_message():
  if cntrl_message == 1:
    rnd=random.randint(1,max_actions) 
    
    #Calculate target
    rndFollow=random.randint(0,len(reTweetSourceList)-1)
    print("rndFollow: " + str(rndFollow))
    followSource=reTweetSourceList[rndFollow]
    print("followSource: " + str(followSource)) 
    
    #Calculate greeting
    rndGreeting=random.randint(0,len(greetingList)-1)
    print("rndGreeting: " + str(rndGreeting))
    greeting=greetingList[rndGreeting]
    print("Greeting: " + str(greeting)) 
    
    #Calculate message
    rndMessage=random.randint(0,len(messageList)-1)
    print("rndMessage: " + str(rndMessage))
    message=messageList[rndMessage]
    print("Message: " + str(message)) 
    
    #Send DM
    my_bot.send_dm(followSource, greeting, message, count=rnd):
    
#Unfolow
def do_unfollow():
  if cntrl_unfollow == 1:
    unfollow_num = accounts * max_actions
    my_bot.auto_unfollow_all_followers(unfollow_num)

#Retweet
def do_retweet():
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
def do_like():
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
    do_retweet()
  elif option == 3:
    print("do_like") 
    do_like()
  else:
    print("do_message") 
    do_message()
 
  #Random Wait
  wait_for = wait_time * random.randint(0, 60)
  print("Waiting for: " + str(wait_for) + " seconds")
  time.sleep(wait_for)
    
    
#my_bot.auto_follow("CNET")    
#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()

print("BOT Finished Process!")
