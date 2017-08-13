from twython import Twython

ConsumerKey = "kaVYVy3MiVQlgmbjNY1c1tXgC"
ConsumerSecret = "U1SlMgkUEhX8fN2rxJNmhRkNL1wrlnYJKZzL6lOnRMMJSotiei"
AccessToken = "3571069213-0GF7pm4jGMA0xnITifvPdIvXYwfjZxc5OELnEBK"
AccessTokenSecret = "veTCGfvmIDfCRDNvDBfj8HGXqnaBBwYCvPxNsJTnvVK6G"



twitter = Twython(ConsumerKey,
ConsumerSecret,
AccessToken,
AccessTokenSecret)

time = twitter.get_user_timeline(screen_name = "jatinja00517709", count = 5)
for tweet in time:
    print(" User: {0} \n Created: {1} \n Text: {2} "
          .format(tweet["user"]["name"].encode('utf-8'),
                  tweet["created_at"].encode('utf-8'),
                  tweet["text"].encode('utf-8')))