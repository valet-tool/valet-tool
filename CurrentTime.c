#include "CurrentTime.h"

void get_current_date_time(char* current_date_time)
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);
	struct timeval time_us;
	char timeInSecs[2];
	char timeInMins[2];
	char timeInHours[2];
	char timeInMsecs[3];
	char month[2];
	char day[2];
	int intTimeInMS = time_us.tv_usec/1000;
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
	if(intTimeInMS<10){
		sprintf(timeInMsecs,"00%d",intTimeInMS);
	}
	else if (intTimeInMS<100 && intTimeInMS>10){
		sprintf(timeInMsecs,"0%d",intTimeInMS);
	}
	else
	{
		sprintf(timeInMsecs,"%d",intTimeInMS);
	}
	
	if(tm.tm_min<10){
		sprintf(timeInMins,"0%d",tm.tm_min);
	}
	else{
		sprintf(timeInMins,"%d",tm.tm_min);
	}

	if(tm.tm_mon+1 < 10){
		sprintf(month,"0%d",tm.tm_mon+1);
	}
	else
	{
		sprintf(month,"%d",tm.tm_mon+1);
	}
	if(tm.tm_mday < 10){
		sprintf(day,"0%d",tm.tm_mday);
	}
	else
	{
		sprintf(day,"%d",tm.tm_mday);
	}
	
	gettimeofday(&time_us, NULL);
	sprintf(current_date_time, "%d-%s-%sT%s:%s:%s.%sZ", 
		 tm.tm_year + 1900, month, day, 
		 timeInHours, timeInMins, 
		 timeInSecs, timeInMsecs);
	
}

