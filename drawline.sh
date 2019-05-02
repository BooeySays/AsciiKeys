#!/bin/bash

DATEFORMAT='%m.%d.%y %H%M HRS'
export THEME_CLR="\033[38;5;9m"
newPS1="$THEME_CLR┗"$RETVAL"$THEME_CLR━ \033[m\\\$ "

function drawps(){
	RET=$?
	RETVAL=$(case $RET in
0)
	echo -en "\033[m\033[01;37m[\033[38;5;10m0\033[01;37m]\033[m"
	;;
*)
	echo -en "\033[m\033[01;37m[\033[01;31m$RET\033[01;37m]\033[m"
	;;
esac)
	screenw=$COLUMNS
	echo
	echo -en "$THEME_CLR┏"
	while [ $screenw -gt 2 ]; do
		echo -en "━"
		((screenw -=1))
	done
	echo -en "━\033[m\r"
#	echo -en "━┗"$RETVAL"\033[01;31m━ \033[m"
#	echo -en "━\033[m\r"
#	tput sc
#	echo -en "\r"
#	tput cuu1
	tput cuf 3
	echo -en "\033[38;5;15m[ \033[m📂\033[01;37m: \033[38;5;226m$(dirs)\033[m\033[38;5;15m ]\r"
	tput cuf $[$[$COLUMNS-$(echo " $(date +"$DATEFORMAT") " | wc -L)]-3]
#	echo -e "[$(date +"%a %b %-d %Y - %-I:%M:%S %p")]"
	echo -e "[$(date +"$DATEFORMAT")]"
	tput rc
#	echo -en "\033[01;31m┗┫\033[m"
#	if [ $RETVAL -eq 0 ]; then
#		echo -en "\033[m\033[01;32m0\033[m"
#	else
#		echo -en "\033[m\033[01;31m$RETVAL\033[m"
#	fi
#	echo -en "\033[01;31m┣━ \033[m"
}
#
#👤
#💻
psbak=$PS1
export PS1=$newPS1