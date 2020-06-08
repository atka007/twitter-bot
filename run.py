from TwitterFollowBot import TwitterBot
import random
import time
import math

my_bot = TwitterBot()
start_time = time.time()

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
repeat_actions = 200
max_actions = 1

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
    #print("rndFollow: " + str(rndFollow))
    followSource=reTweetSourceList[rndFollow]
    print("Follow Source: " + str(followSource))   
        
    my_bot.auto_follow_followers_of_user(followSource, count=rnd)     
        
#Unfolow
def do_unfollow():
  if cntrl_unfollow == 1:
    rnd=random.randint(1,max_actions) 
    my_bot.auto_unfollow_all_followers(rnd)
    
#Retweet
def do_retweet():
  if cntrl_retweet == 1:
    try:
      rnd=random.randint(1,max_actions) 
      rndTweet=random.randint(0,len(reTweetSourceList)-1)
      #print("rndTweet: " + str(rndTweet))
      reTweetSource=reTweetSourceList[rndTweet]
      print("ReTweet Source: " + str(reTweetSource))   
      my_bot.auto_rt(reTweetSource, count=rnd)      
    except:
      print("This didn't work for some reason!")  
      
#Like
def do_like():
  if cntrl_like == 1:
    try:
      rnd=random.randint(1,max_actions) 
      rndLike=random.randint(0,len(likeSourceList)-1)
      #print("rndLike: " + str(rndLike))
      likeSource=likeSourceList[rndLike]
      print("Like Source: " + str(likeSource))
      my_bot.auto_fav(likeSource, count=rnd)      
    except:
      print("This didn't work for some reason!")  
      
#DM
def do_message():
  if cntrl_message == 1:
    rnd=random.randint(1,max_actions) 
    
    #Calculate target
    rndFollow=random.randint(0,len(reTweetSourceList)-1)
    #print("rndFollow: " + str(rndFollow))
    followSource=reTweetSourceList[rndFollow]
    print("Follow Source: " + str(followSource)) 
    
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
    
    
#Run the Loop
for x in range(repeat_actions):
  option = random.randint(0, 3)
  elapsed_time = time.time() - start_time
  
  print("Action Number: ******************  " + str(x) + "  ******************  ")
  #Counters
  print("Followed #: " + str(numFollowed) + " || " + "Unfollowed #: " + str(numUnfollowed) + " || " + "Liked #: " + str(numLiked) + " || " + "Tweeted #: " + str(numTweeted) + " || " + "Messaged #: " + str(numMessaged))
  print("Elapsed Time: " + str(elapsed_time)) 
  
  #do_message()
  
  if option == 0:
    print("Follow Action!")
    do_follow()
    numFollowed += 1

  elif option == 1:
    print("Unfollow Action!")
    do_unfollow()
    numUnfollowed += 1

  elif option == 2:
    print("Retweet Action!")
    do_retweet()
    numTweeted += 1

  elif option == 3:
    print("Like Action!") 
    do_like()
    numLiked += 1

  else:
    print("Message Action!") 
    print("DM not working yet!") 
    #do_message()
    numMessaged += 1
 
  #Random Wait
  wait_for = wait_time * random.randint(2, 60)
  print("Waiting for: " + str(wait_for) + " seconds")
  time.sleep(wait_for)
  
    
    
#my_bot.auto_follow("CNET")    
#my_bot.auto_rt("phrase", count=1000)
#my_bot.auto_unfollow_nonfollowers()
#my_bot.favorite_following_tweets()

print("BOT Finished Process!")
