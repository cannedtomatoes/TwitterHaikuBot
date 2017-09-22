import sys, time, os

sleep_t = 28800 #sleep time in seconds (8 hours)

while True:
	remaining = sleep_t #reset time
	print("Running program")
	os.system('python3 HaikuBookLive.py')
	print("Sleeping for",sleep_t, "seconds")
	
	#Count down seconds until next tweet
	
	while remaining != 0:
		time.sleep(60)
		print(remaining, "seconds remaining until next tweet")
		remaining -= 60