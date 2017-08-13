from twython import Twython

ConsumerKey = "kaVYVy3MiVQlgmbjNY1c1tXgC"
ConsumerSecret = "U1SlMgkUEhX8fN2rxJNmhRkNL1wrlnYJKZzL6lOnRMMJSotiei"
AccessToken = "3571069213-0GF7pm4jGMA0xnITifvPdIvXYwfjZxc5OELnEBK"
AccessTokenSecret = "veTCGfvmIDfCRDNvDBfj8HGXqnaBBwYCvPxNsJTnvVK6G"



twitter = Twython(ConsumerKey,
ConsumerSecret,
AccessToken,
AccessTokenSecret)

followers = twitter.get_followers_list(screen_name="jatinja00517709",count='1')

for follower in followers["users"]:
    print(" user: {0} \n name: {1} \n Number of tweets: {2} \n".format(follower["screen_name"].encode('utf-8'),
                                                                       follower["name"].encode('utf-8'),
                                                                       follower["statuses_count"]))