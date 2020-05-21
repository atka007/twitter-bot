from TwitterFollowBot import TwitterBot
import time
import math
import random

my_bot = TwitterBot()

my_bot.sync_follows()

print("Running Unfollow Bot!")

#Unfolow people
my_bot.auto_unfollow_all_followers(10)
  
#30261067,18286505,18742444,893484744725467137,972651,18927441,14763734,816653,10876852,1344951,275686563,14372486,2890961
print("Unfollow BOT Finished Process!")
