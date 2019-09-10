#!/usr/bin/python

import twitter
import sys
import datetime

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""


DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


class TwitterTimeProfiler():

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret):

            self._api = twitter.Api(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)
            self._api.VerifyCredentials()

    def render(self, day_profile, hour_profile, sample_size):
        # Render Days

        print("\n [>] Day Profile")
        for i in range(0, 7):
            print("\t {}: {}\t {}%".format(
                DAYS[i],
                day_profile[i],
                (day_profile[i]/sample_size)*100 if day_profile[i] > 1 else 0
            ))

        print("\n [>] Hour Profile")
        for i in range(0, 24):
            print("\t {}: {}\t {}%".format(
                i if i > 9 else "0{}".format(i),
                hour_profile[i],
                (hour_profile[i]/sample_size)*100 if hour_profile[i] > 1 else 0
            ))

    def profile(self, username, max_count):

        print(" [?] Profiling {}, please wait.".format(username))

        day_profile = [0]*7
        hour_profile = [0]*24
        count = 0

        since_id = 0
        timeline = self._api.GetUserTimeline(screen_name=username,
                                             count=200,
                                             since_id=0)

        while len(timeline) > 0:
            print(len(timeline))
            print("SinceID: {}".format(since_id))
            for t in timeline:
                day = datetime.datetime.fromtimestamp(
                    t.created_at_in_seconds).weekday()
                hour = datetime.datetime.fromtimestamp(
                    t.created_at_in_seconds).hour

                if t.id > since_id:
                    since_id = t.id
                day_profile[day] += 1
                hour_profile[hour] += 1
                count += 1

            timeline = self._api.GetUserTimeline(screen_name=username,
                                                 count=200,
                                                 since_id=since_id)

        return self.render(day_profile, hour_profile, count)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("{} <Twitter Username> <Sample Count>".format(__file__))
        sys.exit(1)

    print(" [x] Running TweetProfiler")
    tp = TwitterTimeProfiler(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET
    )

    tp.profile(sys.argv[1], int(sys.argv[2]))
