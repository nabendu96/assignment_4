#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int N=10000;
    double x,y;
    float mu=0.5;         //mean

    FILE *data;
	data=fopen("Prob_4.txt","w");                        //storing the numerical result for python plot

    int i;
    for(i=0;i<N;i++)
    {
        x=(double)rand()/(double)RAND_MAX;               //uniform random numbers between 0 and 1
        y=-mu*log(1-x);                                  //transformation method to generate exponential distribution
        fprintf(data,"%e\n",y);
    }

    fclose(data);

	return 0;
    }
