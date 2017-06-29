from twython import Twython
"""
Twitter Python API/Auth
"""
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
"""
Get all English words
"""
def tweet():
    with open('wordsEn.txt') as f:
        englishWords = f.readlines()
    englishWords = [x.strip() for x in englishWords]

    for i in englishWords:
        if i.endswith('s'):
            twitter.update_status(status= 'I hate ' + i)
        else:
            twitter.update_status(status='I hate the ' + i)

tweet()
