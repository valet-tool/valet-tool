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
	char current_date[26];
	uint8_t test_active = 0;
	uint8_t tactic = 0;
	uint32_t delay = 1000000;
	char *message1 = "Thread 1 Download Started!";
	pthread_t thread;
	FILE *file;
	bool file_exists = false;
	char filename[100] = "/home/pi/valet-tool/rawfiles/output-";
	memset(current_date, 0x00, sizeof(current_date) / sizeof(current_date[0]));
	get_current_date(current_date);
	strcat(filename,current_date);
	strcat(filename,".csv");
	char *filenameptr = filename;
	printf("Date,Current(mA),Power(mW),Is_Active,Tactic\n");
	int iret = pthread_create(&thread, NULL, printMsg, (void *)message1);
	file = fopen(filenameptr, "r");
	float current = 0,power = 0;
	if (file != NULL)
	{
		file_exists = true;
		fclose(file);
	}
	if (file_exists == true)
	{
		file = fopen(filenameptr, "a");
	}
	else
	{
		file = fopen(filenameptr, "w+");
	}
	while (keep_running)
	{
		usleep(delay);
		memset(current_date_time, 0x00, sizeof(current_date_time) / sizeof(current_date_time[0]));
		get_current_date_time(current_date_time);
		current = get_current_in_mA(i2c_bus_1_fd);
		power = get_power_in_mW(i2c_bus_1_fd);
		fprintf(file, "%s,%.2f,%.2f\r\n", current_date_time, current, power);
		//printf("%s,%.2f,%.2f\r\n", current_date_time, current, power);
	}
	fclose(file);
	printf("Exiting Gracefully...\n");
	return 0;
}

void *printMsg(void *ptr)
{
	FILE *file_thread,*error_logging_thread;
	char filename[100] = "/home/pi/valet-tool/rawfiles/downstamps-";
	char errorlogfilename[100] = "/home/pi/valet-tool/rawfiles/error-log-";
	bool file_exists = false;
	bool error_file_exists = false;
	int serverNumber = 0,exitcode = 0;
	char current_date_time_thread[26];
	char current_date[26];
	uint32_t delay = 1000000;
	char zipfilename[100]="'LibreOffice_6.2.3_Linux_x86_deb.tar.gz'";
	char debDir[100]= "'LibreOffice_6.2.3_Linux_x86_deb'";
	char filenameArgument[1000]=" '-O' 'LibreOffice_6.2.3_Linux_x86_deb.tar.gz'";
	char wgetCommand[1000]="wget ";
    char link[1000]="";
	char unzipCommand[100]="tar 'xvf' ";
	char zipCommand[100]="tar '-cvzf' 'hello.tar.gz' 'hello.txt'";
	char rmCommand[100]="rm ";
	char grepCommand[100]="grep '-r' 'Hello' '.'";
	memset(current_date, 0x00, sizeof(current_date) / sizeof(current_date[0]));
	get_current_date(current_date);
	strcat(filename,current_date);
	strcat(filename,".csv");
	strcat(errorlogfilename,current_date);
	strcat(errorlogfilename,".csv");
	char *filenameptr = filename;
	char *errorlogfilenameptr = errorlogfilename;
	file_thread = fopen(filenameptr, "r");
	error_logging_thread = fopen(errorlogfilename, "r");
	if (file_thread != NULL)
	{
		file_exists = true;
		fclose(file_thread);
	}
	if (file_exists == true)
	{
		file_thread = fopen(filenameptr, "a");
	}
	else
	{
		file_thread = fopen(filenameptr, "w+");
	}

	if (error_logging_thread != NULL)
	{
		error_file_exists = true;
		fclose(error_logging_thread);
	}
	if (error_file_exists == true)
	{
		error_logging_thread = fopen(errorlogfilenameptr, "a");
	}
	else
	{
		error_logging_thread = fopen(errorlogfilenameptr, "w+");
	}

	signal(SIGINT, sig_handler);
	strcat(rmCommand,zipfilename);
	strcat(unzipCommand,zipfilename);
	while (keep_running)
	{
		int i = 0;
		for (i = 0; i < 9; i++)
		{	
			switch (i)
			{
			case 0:
				strcat(link,"'http://tdf.ufes.br/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 1:
				strcat(link,"'http://tdf.mirror.rafal.ca/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 2:
				strcat(link,"'https://espejito.fder.edu.uy/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 3:
				strcat(link,"'https://mirror.aptus.co.tz/pub/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 4:
				strcat(link,"'http://ftp.kaist.ac.kr/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 5:
				strcat(link,"'https://libreoffice.mirror.garr.it/mirrors/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 6:
				strcat(link,"'http://ftp.bme.hu/pub/mirrors/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 7:
				strcat(link,"'https://mirrors.ucr.ac.cr/tdf/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			case 8:
				strcat(link,"'https://ftp.nluug.nl/office/libreoffice/libreoffice/stable/6.2.3/deb/x86/LibreOffice_6.2.3_Linux_x86_deb.tar.gz'");
				break;
			default:
				printf("Invalid link: Unkown Error Occured!");
				exit(1);
				break;
			}
			strcat(wgetCommand,strcat(link,filenameArgument));
			//Download: tactic 1
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,1, i+1);
			exitcode = system(wgetCommand);
			if(exitcode){
				fprintf(error_logging_thread,"%s,%d,%d,false\n", current_date_time_thread,1,i+1);
			}
			else{
				fprintf(error_logging_thread,"%s,%d,%d,true\n", current_date_time_thread,1,i+1);
			}
			//Placeholder Sleep Tactic 0
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,'0', i+1);
			usleep(delay);

			//Unzip: Tactic 2
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,2, i+1);
			system(unzipCommand);

			//Placeholder Sleep Tactic 0
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,'0', i+1);
			usleep(delay);

			//find command: Tactic 3
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,3, i+1);
			system(grepCommand);

			//Placeholder Sleep Tactic 0
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,'0', i+1);
			usleep(delay);

			//compress command: Tactic 4
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,4, i+1);
			system(zipCommand);

			//Placeholder Sleep Tactic 0
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,'0', i+1);
			usleep(delay);

			// Delete: Tactic 5
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%d,%d\n", current_date_time_thread,5, i+1);
			system(rmCommand);

			//Placeholder Sleep Tactic 0
			//memset(current_date_time_thread, 0x00, sizeof(current_date_time_thread) / sizeof(current_date_time_thread[0]));
			get_current_date_time(current_date_time_thread);
			fprintf(file_thread, "%s,%c,%d\n", current_date_time_thread,'0', i+1);
			usleep(delay);

			// Reset wget command to be able to download again
			strcpy(wgetCommand,"wget ");
			strcpy(link,"");
		}
		
		sleep(30);
	}
	fclose(file_thread);
}
