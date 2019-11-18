#!/usr/bin/env python3

import os
import sys
import shutil

COLUMNS, LINES = shutil.get_terminal_size()
BOXHORZ = '\033[00;01m─\033[m'
BOXVERT = '\033[00;01m│\033[m'
BOXTLa = '\033[00;01m┌\033[m'
BOXTRa = '\033[00;01m┐\033[m'
BOXBLa = '\033[00;01m└\033[m'
BOXBRa = '\033[00;01m┘\033[m'
BOXTLb = '\033[00;01m╭\033[m'
BOXTRb = '\033[00;01m╮\033[m'
BOXBRb = '\033[00;01m╯\033[m'
BOXBLb = '\033[00;01m╰\033[m'
YELLOWCOMMAND = '\033[00;01m╭─ \033[00;01;38;5;190mCOMMAND \033[00;01m─\033[m'

if COLUMNS % 2 != 0:
	BOXWIDTH = (round((COLUMNS-1)*.7)+1)
else:
	BOXWIDTH = round(COLUMNS*.7)

COMMANDSTR = os.getenv('BOXCOMMAND')
EMSPACES = int((COLUMNS - BOXWIDTH)/2)
BOXLIDTOP = (YELLOWCOMMAND + BOXHORZ * (BOXWIDTH - 13) + BOXTRb)
BOXLIDBOT = (BOXBLb + BOXHORZ * (BOXWIDTH - 2) + BOXBRb)
BOXSPACE = (BOXWIDTH - (4 + len(COMMANDSTR)) / 2)
BOXSIDES = (' ' * (BOXWIDTH - 1) + BOXVERT + '\033[' + str(BOXWIDTH) + 'D' + BOXVERT)