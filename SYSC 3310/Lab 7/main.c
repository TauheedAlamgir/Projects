#include "msp.h"
void TA0_N_IRQHandler(void);
void TA1_N_IRQHandler(void);

static int RGB_State = 0; 

int main(void) {
    WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;

    P1->OUT |= (uint8_t)(1 << 0);
    P2->OUT &= (uint8_t)(~((1 << 0)|(1 << 1)|(1 << 2)));	
	  P1->DIR |= (uint8_t)(1 << 0);
    P2->DIR |= (uint8_t)((1 << 0)|(1 << 1)|(1 << 2));
    P1->SEL0 &= (uint8_t)(~(1 << 0));
    P1->SEL1 &= (uint8_t)(~(1 << 0));
    P2->SEL0 &= (uint8_t)(~((1 << 0)|(1 << 1)|(1 << 2)));
    P2->SEL1 &= (uint8_t)(~((1 << 0)|(1 << 1)|(1 << 2)));

		TA0CTL &= (uint16_t) ~(1 << 0); 
		TA0CTL |= (uint16_t)(1 << 1);
		TA0CTL &= (uint16_t)(~((1 << 5) | (1 << 4)));
		TA0CTL &= (uint16_t) (~(1 << 9));
		TA0CTL |= (uint16_t) (1 << 8); 
		TA0CCR0 = 32767;
		TA1CTL &= (uint16_t) ~(1 << 0);
		TA1CTL |= (uint16_t)(1 << 1); 
		TA0CTL |= (uint16_t)(1 << 4);
		TA1CTL &= (uint16_t)(~((1 << 5) | (1 << 4))); 
		TA1CTL &= (uint16_t) (~(1 << 9));
		TA1CTL |= (uint16_t) (1 << 8);
		TA1CCR0 = 16348;
		TA1R = (uint16_t) (16348 - 3277); 
		TA1CTL |= (uint16_t)((1 << 4) | (1 << 5)); 
	
		NVIC_SetPriority(TA0_N_IRQn, 3); 
		NVIC_ClearPendingIRQ(TA0_N_IRQn);
		NVIC_EnableIRQ(TA0_N_IRQn);
	
		NVIC_SetPriority(TA1_N_IRQn, 3); 
		NVIC_ClearPendingIRQ(TA1_N_IRQn);
		NVIC_EnableIRQ(TA1_N_IRQn); 
	
		__ASM("CPSIE I");
	
		while (1) {
			__ASM("WFI");
		}
}

void TA0_N_IRQHandler(void) {
		TA0CTL &= (uint16_t)(~((1 << 0)));
		P1->OUT ^= ((1 << 0)); 	
}

void TA1_N_IRQHandler(void){
		TA1CTL &= (uint16_t) ~((1 << 0)); 
		if(RGB_State != 7){
			RGB_State = 0;
			P2->OUT += (uint16_t) 1;
		}
		else{
			P2->OUT &= ~((1 << 0)| (1 << 1) | (1 << 2));
			RGB_State++;
		}
}

	

