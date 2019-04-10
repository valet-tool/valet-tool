#include "CurrentTime.h"

void get_current_date_time(char* current_date_time)
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	struct timeval time_us;
	gettimeofday(&time_us, NULL);
	 sprintf(current_date_time, "%d-%d-%dT%d:%d:%d:%lu", 
		 tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, 
		 tm.tm_hour, tm.tm_min, 
		 tm.tm_sec, time_us.tv_usec/1000);
	
}

