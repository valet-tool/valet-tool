#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <wiringPi.h>
#include <wiringSerial.h>

char uart_read(int serial_port_fd);
int uart_init(void);

