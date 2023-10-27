#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - a function that runs forever
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main- entry point
 * Return: 0
*/

int main(void)
{
	int child = 0;
	pid_t pid;

	while (child < 5)
	{
		pid = fork();
		if (!pid)
		{
			break;
		}
		printf("Zombie process created, PID: %i\n", (int)pid);
		child++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
