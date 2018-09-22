#used to run as part of a cron task (added with crontab -e)
#add this - changing the path as needed:
#@reboot python /home/pi/mote/python/examples/random-lights.py &
import random

items = ['rainbow', 'static-rainbow', 'test']

random.shuffle(items)

fileToLoad = ('/home/pi/mote/python/examples/{0}.py'.format(items[:1][0]))

print(fileToLoad)

exec(open(fileToLoad).read())