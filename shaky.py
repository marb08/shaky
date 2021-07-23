#!/usr/bin/python3
#
# shaky
#
#
# Version: 0.1
# Author: marb
#

import mouse, time, sys, argparse

def banner():
	print("")
	print("=======================================================")

	print("=======================================================")
	print('''
	 _____ _           _
	/  ___| |         | |
	\ `--.| |__   __ _| | ___   _
	 `--. \ '_ \ / _` | |/ / | | |
	/\__/ / | | | (_| |   <| |_| |
	\____/|_| |_|\__,_|_|\_'\\__, |
	                         __/ |
	                        |___/
		''')
	print(" > shaky.py - marb.................................")
	print("-------------------------------------------------------")
	print("Simple tool to bill while AFK!")
	print("=======================================================")
	print("")

def main():

	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('-h', '--help', action='help', help="Let's shake that mouse, default will jitter the mouse for an undefined amount of time")
	parser.add_argument("-d", "--duration", help="Set the duration of the Mouse jitter in minutes", type=int, metavar="MINUTES")
	args = parser.parse_args()

	banner()

	if args.duration:
		duration=args.duration
		sched_mode(duration)
	else:
		free_mode()

def sched_mode(d):
	t_d=time.time()

	print("Entering in mouse jittering mode, the selected duration is {} minutes ...\nCtrl + C to quit before\n".format(d))
	try:
		t_end = time.time() + 60 * d
		while time.time() < t_end:
			mouse.move(3,0,absolute=False, duration=0.1)
			mouse.move(-3,0,absolute=False, duration=0.1)

			if int(((time.time()-t_d)/60) % 1) == 0:
				print("\rElapsed time {:.2f} minutes".format((time.time()-t_d)//60), end="")

		print("\nDuration interval ended, exiting jitter ...")

	except KeyboardInterrupt:
		print("\nExiting jitter ...")

	print("\rTotal jitter time {:.2f} minutes".format((time.time()-t_d)/60), end="")


def free_mode():

	t_f=time.time()

	y_begin_pos=mouse.get_position()[1]
	y_pos=mouse.get_position()[1]

	try:
		print("Currently in Free jittering mode, press Ctrl + C or move the mouse to exit ...")
		while y_pos == y_begin_pos:
			mouse.move(8,0,absolute=False, duration=0.1)
			mouse.move(0,9,absolute=False, duration=0.1)
			mouse.move(-8,0,absolute=False, duration=0.1)
			mouse.move(0,-9,absolute=False, duration=0.1)
			y_pos=mouse.get_position()[1]

			if int(((time.time()-t_f)/60) % 1) == 0:
				print("\rElapsed time {:.2f} minutes".format((time.time()-t_f)//60), end="")

		print("\nReceived mouse movement, exiting jitter ...")

	except KeyboardInterrupt:
		print("\nExiting jitter ...")

	print("\rTotal jitter time {:.2f} minutes".format((time.time()-t_f)/60), end="")


if __name__ == "__main__":
    main()
