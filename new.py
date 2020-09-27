import tweepy
import random
import time
import math

'''
   The first function serches for a certain keyword and likes the tweets with that keyword.
   The second function follows 50 users of a given account
   The third function unfollows users who dont follow back.
   the three functions are enclosed in a while loop,each function is envoked after 2 hours.
   The access token and authentication handler you get them from your twitter developer account.
   Take care not to violate twitter laws.'''

auth = tweepy.OAuthHandler('8u3rDUSn52nSiVAMnWkhn9OZ4','2rQViPaS9dpIeixx8XBDj2J9Gxhfzk5nTMdXG9MTkrXqKjNV4I')
auth.set_access_token('1085077067140481024-IHYFCPiyGBJ7GfW19nlGqt6A8BfRhg','qr6R5qjqNoBOFWlxiIzeXAztZHQn1LN2eA2ICqYT1t2cR')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()
print (user.name) #prints your name

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




#Timers
start_time = time.time()
wait_time = 1
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


#a variable that hold something you might want to searc on twitter.
def wait():
    wait_for = wait_time * random.randint(2, 60)
    print("Waiting for: " + str(wait_for) + " seconds")
    time.sleep(wait_for)

def do_like():
    print(">> Like Action!")
    rnd=random.randint(1,max_likes) 
    rndLike=random.randint(0,len(likeSourceList)-1)
    #print("rndLike: " + str(rndLike))
    likeSource=likeSourceList[rndLike]
    print("Like Source: " + str(likeSource))
   
    for tweet in tweepy.Cursor(api.search,likeSource).items(1):
        try:
            tweet.favorite()
            time.sleep(5)
            print("Tweet Liked!")         
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def do_retweet():
    print(">> Re-Tweet Action!")
    rnd=random.randint(1,max_actions) 
    rndTweet=random.randint(0,len(reTweetSourceList)-1)
    #print("rndTweet: " + str(rndTweet))
    reTweetSource=reTweetSourceList[rndTweet]
    print("ReTweet Source: " + str(reTweetSource)) 

    for tweet in tweepy.Cursor(api.search,reTweetSource).items(1):
        try:
            tweet.retweet()
            time.sleep(5)
            print("Re-Tweeted!")         
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
           
def do_follow():
    print(">> Follow Action!")
    rnd=random.randint(1,max_actions) 
    rndFollow=random.randint(0,len(followSourceList)-1)
    #print("rndFollow: " + str(rndFollow))
    followSource=followSourceList[rndFollow]
    print("Follow Source: " + str(followSource))                 

    for follower in tweepy.Cursor(api.followers,screen_name=followSource,count=1).items():
        try:
           follower.follow()
           print("Followed:  + str(follower.name) + !") 
        except tweepy.TweepError as e:
           print(e.reason)

def do_unfollow():
    print(">> UnFollow Action!")
    try:
        people = api.followers_ids()
        friends = api.friends_ids()

        friendsList = list(friends)         
        numFollowing = len(friendsList)
        
        for x in range(max_actions):
            rnd=random.randint(1,numFollowing)         
            user_id = friendsList[rnd]  

            if user_id not in people:
                api.destroy_friendship(user_id)
                print("Unfollowed: " + str(user_id)) 

    except tweepy.TweepError as e:
        print(e.reason)

         
def do_message():
    print(">> Message Action!")
    for follower in tweepy.Cursor(api.followers,screen_name=followSource,count=1).items():
     try:
        #follower.follow()
        #message = "Wishing you a day filled with happiness and a year filled with joy. Happy birthday {follower.name}"
        message = "Hello {follower.name}"
        api.send_direct_message(follower,message)
        print("Sent Message!") 
     except tweepy.TweepError as e:
        print(e.reason)

#Run the Loop
for x in range(repeat_actions):
  option = random.randint(0, 4)
  elapsed_time = time.time() - start_time
  
  print("Action Number: ******************  Action #: " + str(x) + "  ******************  ")
  #Counters
  print("Followed #: " + str(numFollowed) + " || " + "Unfollowed #: " + str(numUnfollowed) + " || " + "Liked #: " + str(numLiked) + " || " + "Tweeted #: " + str(numTweeted) + " || " + "Messaged #: " + str(numMessaged))
  #print("Elapsed Time: " + str(elapsed_time))
  print("Elapsed Time: " + str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
      
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
    #print("DM not working yet!") 
    do_message()
    numMessaged += 1
 
  #Random Wait
  wait()
  

'''
#sending Message on birthdays
def AutoBirthdayMessage():
    while(1):
        #opening file which has dates and usernames
        fileName = open('birthdayFile.txt', 'r')

        #getting Current date
        today = time.strftime('%m/%d')

        #checking if there is any dates match from file with current date
        for line in fileName:

            #if day is matched,then send the message to that user.
            if today in line:
                line = line.split(' ')
                user = API.get_user(line[1])
                message = f"Wishing you a day filled with happiness and a year filled with joy. Happy birthday {user.name}"
                API.send_direct_message(user.id, message)
        #loop back after 24hrs
        time.sleep(86400)
        fileName.close()
'''
   
print("BOT Finished Process!")
