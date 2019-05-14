#include "IN219a.h"
#include "CurrentTime.h"
#include "UART_Monitor.h"
int main()
{

	setbuf(stdout, NULL); // Disable stdout buffering
	int i2c_bus_1_fd;
	char *i2c_bus_1 = (char*)"/dev/i2c-1";
	if ((i2c_bus_1_fd = open(i2c_bus_1, O_RDWR)) < 0)
	{
		printf("Failed to open the i2c bus");
		return -1;
	}

	/* Set I2C_SLAVE for adapter 1 */
	if (ioctl(i2c_bus_1_fd, I2C_SLAVE, IN219A_I2C_ADDRESS) < 0)
	{
		printf("Failed to aquire I2C bus or communicate with device at address: %x.\r\n", IN219A_I2C_ADDRESS);
		return -1;
	}
	IN219A_reset(i2c_bus_1_fd);
	int serial_port_fd = uart_init();
	char current_date_time[26];
	uint8_t test_active = 0;
	uint32_t delay = 1000000;
	printf("Date,Current(mA),Power(mW),Is_Active");
	while (1)
	{
		usleep(delay);
		memset(current_date_time, 0x00, sizeof(current_date_time)/sizeof(current_date_time[0]));
		get_current_date_time(current_date_time);
		switch(uart_read(serial_port_fd))
		{
		case 'B':
			test_active = 1;
			delay = 50000;
			break;
		case 'E':
			delay = 1000000;
			test_active = 0;
			break;
		}
		printf("%s,%.2f,%.2f,%d,\r\n", 
			current_date_time, get_current_in_mA(i2c_bus_1_fd), 
			get_power_in_mW(i2c_bus_1_fd),test_active);
	 }

	return 0;
}

