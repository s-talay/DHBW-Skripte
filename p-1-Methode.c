#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <stdint.h>
#include <inttypes.h>
#include <time.h>

bool istPrim(uint64_t n){
	if(n < 2){
		return false;
	}
	for(uint64_t i = 2; i < floor(sqrt(n)); i++){
		if(n%i == 0){
			return false;
		}
	}
	return true;
}

uint64_t ggT(uint64_t a,uint64_t b){
	uint64_t temp;
	while(b){
		temp = a;
		a = b;
		b = temp%b;
	}
	return a;
}

uint64_t findeFaktor(uint64_t n){
	uint8_t a = 2;
	uint64_t exp = 2;
	while(n%2 == 0){
		return 2;
	}
	while(true){
		uint64_t g = ggT(pow(a,exp)-1,n);
		if(g > 1){
			printf("Faktor gefunden: %"PRIu64"\n",g);
			return g;
		}
		exp++;
	}
}

void pMinus1(uint64_t* array, uint64_t n, int* faktorcount){
	uint64_t faktor;
	int i = 0;
	while(true){
		faktor = findeFaktor(n);
		array[i] = faktor;
		n = n/faktor;
		printf("n: %"PRIu64"\n",n);
		i++;
		(*faktorcount)++;

		if(n == 1){
			return;
		}
	}
}

int main(int argc, char **argv) {

	uint64_t num = 184467440737095516;

	int size = 1024*sizeof(uint64_t);
	uint64_t* array = malloc(size);
	int faktorcount = 0;
	int* ptr = &faktorcount;
	if(array == NULL){
		printf("Fehler: Konnte kein Speicher vom System erhalten.");
		return 1;
	}
	double start_time = clock();
	pMinus1(array, num,ptr);
	double end_time = clock();
	double zeitInS = (double)(end_time-start_time)/CLOCKS_PER_SEC;
	printf("Faktoren: [");
	for(int i = 0; i<faktorcount;i++){
		printf("%"PRIu64,array[i]);
		if(i != faktorcount-1){
			printf(",");
		}
	}
	printf("]\n");
	printf("Faktorcount: %d\n",faktorcount);
	printf("Benötigte Zeit: %fs\n",zeitInS);
	free(array);
	return 0;
}
