#include <stdio.h>
#include <unistd.h>

int main(){
	int i;
	for(i=0;i<4;i++){
		printf("[ %d Term ]\t",i);
		fork();
		printf("%d\n",getpid());
	}
	return 0;
}
