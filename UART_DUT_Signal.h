#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <wiringPi.h>
#include <wiringSerial.h>

void uart_write(int serial_port_fd, char data);
int uart_init(void);

