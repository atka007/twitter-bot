from TwitterFollowBot import TwitterBot
import random
import time
import math

my_bot = TwitterBot()
start_time = time.time()

#Lists
followSourceList = ["DJBritStar","MarkusDupree","BrianaBanderas","autumnfallsxoxo","janewildexxx","karleegreyxxx","lindasteelehot1","emilywillisxoxo","TinaKayxxx",
                  "DreddXXX","Pornhub","AsaAkira","slutsaucekhloe","syrendemerxxx","AlenaCroftXXX","_rush187_","natasha__10_","Katyuskamoonfox","alexgreyxxx",
                  "KenzieReevesxxx","kj_fetishmodel","Kayden_Kross","jonnidarkko","EMMAHIXOFFICIAL","CanelaSKinOff","livejasmin","EvilAngelVideo","Brazzers","blacked_com",
                  "tushy_com","vixen","deeper_official","AVNMediaNetwork","AdultBrazil","legal_porno","JulesJordan","sluttyangelss","pervcity","legalpornocz","xhamstercom"]
reTweetSourceList = ["EvilAngelVideo","livejasmin","Brazzers","blacked_com","tushy_com","vixen","deeper_official","AVNMediaNetwork","AdultBrazil","legal_porno",
                     "JulesJordan","sluttyangelss","pervcity","legalpornocz","xhamstercom"]
likeSourceList = ["DJBritStar","MarkusDupree","BrianaBanderas","autumnfallsxoxo","janewildexxx","karleegreyxxx","lindasteelehot1","emilywillisxoxo","TinaKayxxx",
                  "DreddXXX","Pornhub","AsaAkira","slutsaucekhloe","syrendemerxxx","AlenaCroftXXX","_rush187_","natasha__10_","Katyuskamoonfox","alexgreyxxx",
                  "KenzieReevesxxx","kj_fetishmodel","Kayden_Kross","jonnidarkko","EMMAHIXOFFICIAL","CanelaSKinOff","livejasmin","EvilAngelVideo","Brazzers","blacked_com",
                  "tushy_com","vixen","deeper_official","AVNMediaNetwork","AdultBrazil","legal_porno","JulesJordan","sluttyangelss","pervcity","legalpornocz","xhamstercom"]

#greetingList = ["Hey", "Hi", "Hello"]
#messageList = ["please follow us @feed_gift !","you must check us out @feed_gift !",
#               "have you heard of www.gift-feed.com? Please follow us @feed_gift to learn more!"]

greetingList = [""]
messageList = ["",
               "",
               "",
               ""]


#Timers
wait_time = 6
repeat_actions = 100
max_actions = 1
max_likes = 2

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
    
    rndFollow=random.randint(0,len(followSourceList)-1)
    #print("rndFollow: " + str(rndFollow))
    followSource=followSourceList[rndFollow]
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
      rnd=random.randint(1,max_likes) 
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
  #print("Elapsed Time: " + str(elapsed_time))
  print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
    
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
