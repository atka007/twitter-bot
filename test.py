from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()

my_bot.sync_follows()
my_bot.send_tweet("Hello world!")
