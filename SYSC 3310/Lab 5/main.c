#include "msp.h"

int DELAY_VALUE = 100000;

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
	
	P1IES |= (uint8_t)0x02;
	P1IFG &= (uint8_t)~0x02;
	P1IE |= (uint8_t)0x02;
	
	NVIC_SetPriority(PORT1_IRQn, 2);
	NVIC_ClearPendingIRQ(PORT1_IRQn);
	NVIC_EnableIRQ(PORT1_IRQn);
	
	__ASM("CPSIE I");
	
	while(1){}
		return 0;
}

void PORT1_IRQHandler(void){
	int LED = 0;
	uint8_t rgb = 0;
	int i = DELAY_VALUE;
	while(1) {
		int i = DELAY_VALUE;
		while((P1->IN & (uint8_t)(1<<1))&&(P1->IN & (uint8_t)(1<<4))){}

		while (i>0){
			i--;
		}
		if(!(P1IN & (uint8_t)(1<<1))){ 
			P1->OUT ^= 0x01;
				
			}
		 else if(!(P1IN & (uint8_t)(1<<4))){ 
				if (!LED){
					P2OUT = (rgb % 8);
					rgb++;
					continue;
				}
		}
	}
}



