from twython import Twython

ConsumerKey = "kaVYVy3MiVQlgmbjNY1c1tXgC"
ConsumerSecret = "U1SlMgkUEhX8fN2rxJNmhRkNL1wrlnYJKZzL6lOnRMMJSotiei"
AccessToken = "3571069213-0GF7pm4jGMA0xnITifvPdIvXYwfjZxc5OELnEBK"
AccessTokenSecret = "veTCGfvmIDfCRDNvDBfj8HGXqnaBBwYCvPxNsJTnvVK6G"



twitter = Twython(ConsumerKey,
ConsumerSecret,
AccessToken,
AccessTokenSecret)
result = twitter.search(q="PrabhasRaju",count='10',lang="en")

#for status in result["statuses"]:
 #       print(status)
for status in result["statuses"]:
    print("\nuser: {0}\ntext: {1}\ntime: {2}".format(status["user"]["name"].encode('utf-8'),status["text"].encode('utf-8'),status["created_at"]))
    #print (status)