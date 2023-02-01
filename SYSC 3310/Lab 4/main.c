#include "msp.h"




int main(void){
	WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;
	
	P1->OUT |= (uint8_t)((1 << 1) | (1 << 4));
	P1->SEL0 &= (uint8_t)(~((1 << 1) | (1 << 4)));
	P1->SEL1 &= (uint8_t)(~((1 << 1) | (1 << 4)));
	P1->REN |= (uint8_t)(((1 << 1) | (1 << 4)));
	P2->SEL0 &= (uint8_t)(~((1 << 0) | (1 << 1) | (1 << 2)));
	P2->SEL1 &= (uint8_t)(~((1 << 0) | (1 << 1) | (1 << 2)));
	
	P1->DIR &= (uint8_t)(~((1 << 1) | (1 << 4)));
	P1->DIR |= (uint8_t)((1 << 0));
	P2->DIR |= (uint8_t)((1 << 0) | (1 << 1) | (1 << 2));
	
	P1->DS &= (uint8_t)(~(1 << 0));
	P2->DS &= (uint8_t)(~((1 << 0) | (1 << 1) | (1 << 2)));
	
	P1->OUT &= (uint8_t)(~(1 << 0));
	P2->OUT &= (uint8_t)(~((1 << 0) | (1 << 1) | (1 << 2)));
	
	while(1) {

		while((P1->IN & (uint8_t)(1<<1))&&(P1->IN & (uint8_t)(1<<4))){}

			if(!(P1->IN & (uint8_t)(1<<1))){
					P1->OUT ^= 0x01;
			}
		}
	}
