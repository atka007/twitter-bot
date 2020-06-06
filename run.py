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

#greetingList = ["Hey", "Hi", "Hello"]
#messageList = ["please follow us @feed_gift !","you must check us out @feed_gift !",
#               "have you heard of www.gift-feed.com? Please follow us @feed_gift to learn more!"]

greetingList = [""]
messageList = ["Yes, gifting is a form of love language. During this hard times, nothing beats genuine gesture of love and care by sending our loved ones gifts for all occasion from @feed_gift!",
               "No parties, no problem! Show your loved one you still care by sending them exciting gifts from @feed_gift ! Check out as there are tons of new items everyday!",
               "Father's day is coming soon!!! Get your dad, partner, husband, brother and uncles the best, craziest and most affordable gift from @feed_gift!",
               "Can't give hugs and kisses via Zoom?! Check out @feed_gift for variety of gift items you can give to your loved ones."]

#Timers
wait_time = 4
repeat_actions = 30

#Counters
numFollowed = 0
numUnfollowed = 0
numLiked = 0
numTweeted = 0
numMessaged = 0

#Controls
cntrl_follow = 1
cntrl_unfollow = 1
cntrl_retweet = 1
cntrl_like = 1
cntrl_message = 0

daily_actions = repeat_actions * wait_time
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
    numFollowed = numFollowed + 1
    
#DM
def do_message():
  if cntrl_message == 1:
    rnd=random.randint(1,max_actions) 
    
    #Calculate target
    rndFollow=random.randint(0,len(reTweetSourceList)-1)
    #print("rndFollow: " + str(rndFollow))
    followSource=reTweetSourceList[rndFollow]
    print("followSource: " + str(followSource)) 
    
    #Calculate greeting
    rndGreeting=random.randint(0,len(greetingList)-1)
    #print("rndGreeting: " + str(rndGreeting))
    greeting=greetingList[rndGreeting]
    #print("Greeting: " + str(greeting)) 
    
    #Calculate message
    rndMessage=random.randint(0,len(messageList)-1)
    #print("rndMessage: " + str(rndMessage))
    message=messageList[rndMessage]
    #print("Message: " + str(message)) 
    
    #Send DM
    my_bot.send_dm(followSource, greeting, message, count=rnd)
    numMessaged = numMessaged + 1
    
#Unfolow
def do_unfollow():
  if cntrl_unfollow == 1:
    unfollow_num = accounts * max_actions
    my_bot.auto_unfollow_all_followers(unfollow_num)
    numUnfollowed = numUnfollowed + 1


#Retweet
def do_retweet():
  if cntrl_retweet == 1:
    try:
      rndTweet=random.randint(0,len(reTweetSourceList)-1)
      print("rndTweet: " + str(rndTweet))
      reTweetSource=reTweetSourceList[rndTweet]
      print("reTweetSource: " + str(reTweetSource))   
      my_bot.auto_rt(reTweetSource, count=retweets)
      numTweeted = numTweeted + 1
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
      numLiked = numLiked + 1
    except:
      print("This didn't work for some reason!")  


for x in range(repeat_actions):
  print("Action Number: ******************  " + str(x) + "  ******************  ")
  #Counters
  print("Followed Number: " + str(numFollowed))
  print("Unfollowed Number: " + str(numUnfollowed))
  print("Liked Number: " + str(numLiked))
  print("Tweeted Number: " + str(numTweeted))
  print("Messaged Number: " + str(numMessaged))
      
  option = random.randint(0, 4)
  
  #do_message()
  
  if option == 0:
    print("do_follow")
    do_follow()
  elif option == 1:
    print("do_unfollow")
    do_unfollow()
  elif option == 2:
    print("do_retweet")
    do_retweet()
  elif option == 3:
    print("do_like") 
    do_like()
  else:
    print("do_message") 
    print("DM not working yet!") 
    #do_message()
 
  #Random Wait
  wait_for = wait_time * random.randint(2, 60)
  print("Waiting for: " + str(wait_for) + " seconds")
  time.sleep(wait_for)
  
    
    
#my_bot.auto_follow("CNET")    
#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()

print("BOT Finished Process!")
