import sys, time, os

sleep_t = 1800 #sleep time in seconds

while True:
	remaining = sleep_t #reset time
	print("Running program")
	os.system('python3 HaikuBookLive.py')
	print("Sleeping for",sleep_t, "seconds")
	
	#Count down seconds until next tweet
	
	while remaining != 0:
		time.sleep(1)
		print(remaining, "seconds remaining until next tweet")
		remaining -= 1