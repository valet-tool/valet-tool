#include "UART_DUT_Signal.h"


int main (int argc, char **argv)
{
	if (argc != 2)
	{
		fprintf(stdout, "Incorrect Prms provided. exiting...%s\r\n", strerror(errno));
		return -1;
	}
	else if (strlen(argv[1]) != 1) 
	{
        	fprintf(stderr, "Invalid argument '%s'\n", argv[1]);
        	return -2;
    	}
	int serial_port_fd = uart_init();
	switch(argv[1][0])
	{
	case 'B':
	case 'b':
		uart_write(serial_port_fd, 'B');
		break;
	case 'E':
	case 'e':
		uart_write(serial_port_fd, 'E');	
		break;
	default:
		fprintf(stderr, "Incorrect char prm: %s\r\n", strerror(errno));
		return -3;
	}
	return 0;
}

int uart_init()
{
  	int serial_port_fd;
  	if ((serial_port_fd = serialOpen("/dev/ttyAMA0", 9600)) < 0)	
  	{
    		fprintf(stderr, "Unable to open serial console: %s\r\n", strerror(errno));
    		return -4 ;
  	}	
  	if (wiringPiSetup() == -1)					
  	{
    		fprintf(stderr, "WiringPi Init has failed: %s\r\n", strerror(errno));
    		return -5 ;
  	}
	return serial_port_fd;

}

void uart_write(int serial_port_fd, char data)
{
	serialPutchar(serial_port_fd, data);		
}

