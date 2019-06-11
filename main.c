#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "pthread.h"
#include "stdbool.h"
#include "string.h"
#include "IN219a.h"
#include "CurrentTime.h"
#include "UART_Monitor.h"

void *printMsg(void *ptr);
static volatile sig_atomic_t keep_running = 1;

static void sig_handler(int _)
{
	(void)_;
	keep_running = 0;
}

int main()
{

	setbuf(stdout, NULL); // Disable stdout buffering
	int i2c_bus_1_fd;
	char *i2c_bus_1 = (char *)"/dev/i2c-1";
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
	uint8_t tactic = 0;
	uint32_t delay = 1000000;
	char *message1 = "Thread 1 Download Started!";
	pthread_t thread;
	FILE *file;
	bool file_exists = false;
	const char *filename = "output.csv";
	printf("Date,Current(mA),Power(mW),Is_Active,Tactic\n");
	int iret = pthread_create(&thread, NULL, printMsg, (void *)message1);
	file = fopen(filename, "r");
	if (file != NULL)
	{
		file_exists = true;
		fclose(file);
	}
	if (file_exists == true)
	{
		file = fopen(filename, "a");
	}
	else
	{
		file = fopen(filename, "w+");
	}
	while (keep_running)
	{
		usleep(delay);
		memset(current_date_time, 0x00, sizeof(current_date_time) / sizeof(current_date_time[0]));
		get_current_date_time(current_date_time);
		fprintf(file, "%s,%.2f,%.2f\r\n", current_date_time,
				get_current_in_mA(i2c_bus_1_fd), get_power_in_mW(i2c_bus_1_fd));
		printf("%s,%.2f,%.2f\r\n", current_date_time,
			   get_current_in_mA(i2c_bus_1_fd), get_power_in_mW(i2c_bus_1_fd));
	}
	fclose(file);
	printf("Exiting Gracefully...\n");
	return 0;
}

void *printMsg(void *ptr)
{
	FILE *file_thread;
	const char *filename = "downstamps.csv";
	bool file_exists = false;
	int serverNumber = 0;
	char current_date_time_thread[26];
	file_thread = fopen(filename, "r");
	if (file_thread != NULL)
	{
		file_exists = true;
		fclose(file_thread);
	}
	if (file_exists == true)
	{
		file_thread = fopen(filename, "a");
	}
	else
	{
		file_thread = fopen(filename, "w+");
	}

	signal(SIGINT, sig_handler);
	char zero='0';
	while (keep_running)
	{
		int i = 0;
		for (i = 0; i <= 0; i++)
		{
			//Download: tactic 1
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,1, i+1);
			system("wget 'http://tdf.ufes.br/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz' '-O' 'LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
			
			//Placeholder Sleep Tactic 0
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,zero, i+1);
			sleep(1);

			//Unzip: Tactic 2
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,2, i+1);
			system("tar 'xvf' 'LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");

			//Placeholder Sleep Tactic 0
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,zero, i+1);
			sleep(1);

			//Bla Bla Tactic 3
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,3, i+1);
			sleep(1);

			//Placeholder Sleep Tactic 0
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,zero, i+1);
			sleep(1);

			// Delete: Tactic 5
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,5, i+1);
			system("rm 'LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");

			//Placeholder Sleep Tactic 0
			memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,zero, i+1);
			sleep(1);
	
		}
		
		sleep(30);
	}
	fclose(file_thread);
}
