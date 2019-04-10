#include "UART_Monitor.h"

int uart_init()
{
  int serial_port_fd;
  if ((serial_port_fd = serialOpen("/dev/ttyS0", 9600)) < 0)	
  {
    fprintf(stderr, "Unable to open serial console: %s\r\n", strerror(errno)) ;
    return -1 ;
  }

  if (wiringPiSetup() == -1)					
  {
    fprintf(stdout, "WiringPi Init has failed: %s\r\n", strerror(errno)) ;
    return -1 ;
  }
  return serial_port_fd;

}

char uart_read(int serial_port_fd)
{
	  
	if(serialDataAvail(serial_port_fd))
	{ 
		return serialGetchar(serial_port_fd);		
	//	serialPutchar(serial_port, dat);		
	}
	return 0x00;

}
