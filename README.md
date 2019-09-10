# TwitterProfiler

This is a simple script that does time based profiling of a users tweets.

I have used this in the past to detect bot usage, or habitual patterns of twitter users.

Interesting patterns i have found are things like:

    - Commuters: People that only tweet on their way too and from work (Nice timezone attribution)
    - Bots: Perfectly normalized distribution, either 24/7/365 or Monday-Friday
    - Weekend Warriors: Accounts that only tweet at the weekend

Feel free to use this script as you wish.

## Usage

You will need to register a twitter app to get the following API keys for tspy.py:

    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_TOKEN_KEY = ""
    ACCESS_TOKEN_SECRET = ""

Once those are set, you should be able to install the dependencies and run:

    pip install -r requirements.txt
    ./tspy.py <Twitter Username> <Sample Count>

## Example Output

    (env) C02V402XHTD7:TwitterTime adambradbury$ python tspy.py AdamTheAnalyst 200
     [x] Running TweetProfiler
     [?] Profiling AdamTheAnalyst, please wait.
    200
    SinceID: 0

     [>] Day Profile
         Mon: 49	 24.5%
         Tue: 39	 19.5%
         Wed: 32	 16.0%
         Thu: 38	 19.0%
         Fri: 29	 14.499999999999998%
         Sat: 6	 3.0%
         Sun: 7	 3.5000000000000004%

     [>] Hour Profile
         00: 0	 0%
         01: 0	 0%
         02: 0	 0%
         03: 0	 0%
         04: 0	 0%
         05: 7	 3.5000000000000004%
         06: 13	 6.5%
         07: 31	 15.5%
         08: 25	 12.5%
         09: 11	 5.5%
         10: 16	 8.0%
         11: 8	 4.0%
         12: 16	 8.0%
         13: 10	 5.0%
         14: 7	 3.5000000000000004%
         15: 17	 8.5%
         16: 13	 6.5%
         17: 9	 4.5%
         18: 7	 3.5000000000000004%
         19: 3	 1.5%
         20: 0	 0%
         21: 7	 3.5000000000000004%
         22: 0	 0%
         23: 0	 0%