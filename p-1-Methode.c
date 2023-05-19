#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <stdint.h>

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
			printf("Faktor gefunden: %llu\n",g);
			return g;
		}
		exp++;
	}
}

uint64_t* pMinus1(uint64_t n){
	
}

int main(int argc, char **argv) {

}
