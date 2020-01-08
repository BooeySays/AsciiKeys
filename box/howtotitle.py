#!/usr/bin/env python3

import shutil, sys, os, argparse, random

rancolor = random.randint(16,232)
bordercolor = None
cursorhide = '\033[?25l'
cursorshow = '\033[?25h'
colormapinit = 16

parser = argparse.ArgumentParser()

parser.add_argument('-c', '--color', dest="colorarg", help="Sets border color (Default: random)")
parser.add_argument('-b', '--bold', dest="boldborder", action="store_true", default="False", help="Draws bold borders")

args = parser.parse_args()

COLS, LINES = shutil.get_terminal_size()

if args.colorarg == None:
	bordercolor = ('\033[38;5;' + str(rancolor) + 'm')
else:
	bordercolor = ('\033[38;5;' + str(args.colorarg) + 'm')

if args.boldborder == True:
	bordercolor = (bordercolor + '\033[01m')

BORDERTOP = (bordercolor + '╭' + '─' * int(COLS - 2) + '╮\033[m')
BORDERBOD = (bordercolor + '│\033[' + str(COLS) + 'C│\033[m')
BORDERBOT = (bordercolor + '╰' + '─' * int(COLS - 2) + '╯\033[m')

def drawbord():
	hgt = (LINES - 2)
	print(cursorhide)
	print(BORDERTOP)
	while hgt > 0:
		print(BORDERBOD)
		hgt -= 1
	print(BORDERBOT,end='')
	print(cursorshow,end='')
	input('')

def drawcolormap():
	count = int(colormapinit)
	while count < 232:
		countline = 7
		while countline > 0:
			print('   \033[' + str(len((count)) + 'D' + str(count) + ': \033[48;5;' + str(count) + 'm  \033[m ',end='')
			count += 1
			countline -= 1
		print('\n')

drawcolormap()
#drawbord()