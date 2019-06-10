#include "CurrentTime.h"

void get_current_date_time(char* current_date_time)
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	struct timeval time_us;
	char timeInSecs[2];
	char timeInMins[2];
	char timeInHours[2];
	if(tm.tm_hour<10){
		sprintf(timeInHours,"0%d",tm.tm_hour);
	}
	else{
		sprintf(timeInHours,"%d",tm.tm_hour);
	}
	if(tm.tm_sec<10){
		sprintf(timeInSecs,"0%d",tm.tm_sec);
	}else{
		sprintf(timeInSecs,"%d",tm.tm_sec);
	}
	if(tm.tm_min<10){
		sprintf(timeInMins,"0%d",tm.tm_min);
	}
	else{
		sprintf(timeInMins,"%d",tm.tm_min);
	}

	gettimeofday(&time_us, NULL);
	sprintf(current_date_time, "%d-%d-%dT%s:%s:%s:%lu", 
		 tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, 
		 timeInHours, timeInMins, 
		 timeInSecs, time_us.tv_usec/1000);
	
}

