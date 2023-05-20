#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>
#include <time.h>

#define BLOCK_SIZE sizeof(uint32_t)
#define ERROR 	if (!hash) {printf("Speicherallokation fehlgeschlagen.\n");return NULL;	}

uint32_t Q(uint32_t input);
void test();
uint32_t rot_left(uint32_t num, uint32_t rot);
uint32_t s_0 = 0x524f464c;
uint32_t abcd = 0x632e4e5c;

int main(int argc, char **argv) {
//	test();
	clock_t start_time,end_time;
	start_time = clock();
	for(uint32_t i = 0;i < 0xFFFFFFFF; ++i){
		if(Q(i) == abcd){
			printf("Gefunden: %x\n",i);
			end_time = clock();
			double time = (double)(end_time-start_time)/CLOCKS_PER_SEC;
			printf("Zeit: %fs\n",time);
		}
	}
	return 1;
}

void test(){
	uint32_t q1 = Q(s_0);
	uint32_t q2 = Q(Q(s_0));
	uint32_t q3 = Q(Q(Q(s_0)));

	printf("q1: %x\n",q1);
	printf("q2: %x\n",q2);
	printf("q3: %x\n",q3);
}

uint32_t Q(uint32_t input) {
	return input ^ rot_left(input, 17);
}


uint32_t rot_left(uint32_t num, uint32_t rot) {
    return ((num << rot) | (num >> (32 - rot)));
}

