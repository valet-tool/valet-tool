all: PiMonitor PiDUT
PiMonitor: main.c UART_Monitor.c CurrentTime.c IN219a.c
	gcc -o PiMonitor UART_Monitor.c CurrentTime.c IN219a.c main.c -lwiringPi -lpthread 
PiDUT: UART_DUT_Signal.c 
	gcc -o PiDUTSignal UART_DUT_Signal.c -lwiringPi
clean: SHELL:=/bin/bash
clean:
	if [ -e ./PiMonitor ]; then rm -f PiMonitor; fi 
	if [ -e ./PiDUTSignal ]; then rm -f PiDUTSignal; fi	
