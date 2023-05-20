#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <string.h>

//Keys
uint16_t k1 = 0x1aa2;
uint16_t k2 = 0x2bb3;
uint16_t k3 = 0x3cc4;


//4 bit von little endian zu big endian
uint8_t reverseOrder(uint8_t b) {
    uint8_t b1 = (b & 0b1000) >> 3;
    uint8_t b2 = (b & 0b0100) >> 1;
    uint8_t b3 = (b & 0b0010) << 1;
    uint8_t b4 = (b & 0b0001) << 3;
    return (b1 | b2 | b3 | b4);
}
//SBox
uint8_t sBox(uint8_t b) {
    uint8_t liste[] = {0x4, 0x3, 0x9, 0xa, 0xb, 0x2, 0xe, 0x1,0xd, 0xc, 0x8, 0x6, 0x7, 0x5, 0x0, 0xf};
    return liste[b];
}

uint16_t F(uint16_t R, uint16_t K) {
    uint8_t B1 = R & 0x000F;
    uint8_t B2 = (R & 0x00F0) >> 4;
    uint8_t B3 = (R & 0x0F00) >> 8;
    uint8_t B4 = (R & 0xF000) >> 12;

    uint8_t block1 = reverseOrder(B4);
    uint8_t block4 = reverseOrder(B1);
    uint8_t block2 = sBox(B2);
    uint8_t block3 = sBox(B3);

    return ((block4 << 12) | (block3 << 8) | (block2 << 4) | (block1 << 0)) ^ K;
}

uint32_t runde(uint32_t I, uint16_t K) {
    uint16_t InL = I >> 16;
    uint16_t InR = I & 0x0000FFFF;
    uint16_t OutR = InL ^ F(InR, K);
    uint16_t OutL = InR;
    return (OutL << 16) | OutR;
}
//fast indetisch mit Runde bis aus L R swap, weil von hinten angefangen wird
uint32_t rundeRev(uint32_t I, uint16_t K) {
    uint16_t InL = I >> 16;
    uint16_t InR = I & 0x0000FFFF;
    //ab hier L R tauschen relativ zu normale runde
    uint16_t OutL = InR ^ F(InL, K);
    uint16_t OutR = InL;
    return (OutL << 16) | OutR;
}

uint32_t enc(uint32_t P) {
    uint32_t r1 = runde(P, k1);
    uint32_t r2 = runde(r1, k2);
    uint32_t r3 = runde(r2, k3);
    return r3;
}
//fast identisch mit enc, nur wird rundeRev verwendet
uint32_t dec(uint32_t C) {
    uint32_t r1 = rundeRev(C, k3);
    uint32_t r2 = rundeRev(r1, k2);
    uint32_t r3 = rundeRev(r2, k1);
    return r3;
}

int main() {
	//Testwerte
    uint32_t P1 = 0x12345678;
    uint32_t C1 = enc(P1);
    uint32_t PP = dec(C1);

    printf("Testwerte:\n");

    printf("I = %04x, K = %04x: F(I,K) = %04x\n",0x1234,0x0000,F(0x1234,0x0000));
    printf("I = %04x, K = %04x: F(I,K) = %04x\n",0x1234,0x2345,F(0x1234,0x2345));
    printf("I = %04x, K = %04x: F(I,K) = %04x\n",0xabcd,0xbeef,F(0xabcd,0xbeef));
    printf("I = %04x, K = %04x: F(I,K) = %04x\n",0x9876,0xfedc,F(0x9876,0xfedc));
    printf("%08x wird encoded zu %08x\n", P1, C1);
    printf("%08x wird decoded zu %08x\n", C1, PP);

    printf("\n");

	//Aufgabe 1
    printf("Aufgabe 1\n");
    uint32_t P = 0xabcd0815;
    printf("%08x wird encoded zu %08x\n",P, enc(P));

    //Aufgabe 2
    printf("Aufgabe 2\n");
    uint32_t C = 0x12345678;
    printf("%08x wird decoded zu %08x\n", C, dec(C));

    return 0;
}
