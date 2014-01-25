nethack-expect-wiz
==================
This is a Nethack start scumming bot.


Features:
==================
1) It has three conditions, so you can get it fast: In:18, Magic Missile, and Ring of slow digestion. (You still can add more conditions, such as another ring)

2) It runs fast and stable. Every time your computer's random seed changes, it can run two to three times to scum. It means that, you will never miss any single random seed changing.

System requirement:
==================
1) Linux or other Posix compatible system

2) We do not provide package, to download, you need git. (Official website: http://git-scm.com/)

3) Python 2.7 (Most Linux distributions install it by default)

4) pexpect (official website: http://pexpect.readthedocs.org/en/latest/)

5) Well installed Nethack(should be install properly in your /usr or /usr/local)

For more information, please read: http://wealthlibre.info/blog/nethack-and-its-start-scumming and http://wealthlibre.info/blog/20140109-update-of-nethack-start-scumming-bot

Installation:
==================
$ git clone https://github.com/bolan/nethack-expect-wiz

$ cd nethack-expect-wiz

Usage:
==================
$ python nh-expect-wiz.py

On your running console, 0 means that you got the stuff, 1 means that you did not get the stuff. Once you get all the conditions -- the "expected wizard", you will see "You get an expected Wizard." at the bottom of your Unix console. You can run your nethack on a normal way.
