from twython import Twython

ConsumerKey = "kaVYVy3MiVQlgmbjNY1c1tXgC"
ConsumerSecret = "U1SlMgkUEhX8fN2rxJNmhRkNL1wrlnYJKZzL6lOnRMMJSotiei"
AccessToken = "3571069213-0GF7pm4jGMA0xnITifvPdIvXYwfjZxc5OELnEBK"
AccessTokenSecret = "veTCGfvmIDfCRDNvDBfj8HGXqnaBBwYCvPxNsJTnvVK6G"



twitter = Twython(ConsumerKey,
ConsumerSecret,
AccessToken,
AccessTokenSecret)

result = twitter.get_place_trends(id =23424977)

if result:
    for trend in result[0].get("trends", []):
        print("{0}\n".format(trend["name"].encode('utf-8')))


#WOEID(Bombay)=2295411
#WOEID(us)=23424977