// Tauheed Alamgir 101194927

/* fraction.c - SYSC 2006 Lab 5 */

#include <stdlib.h>  // abs(x)
#include <stdio.h>   // printf
#include <assert.h>  // assert

#include "fraction.h"

/* Print the fraction pointed to by pf in the form a/b. 
 */
void print_fraction(const fraction_t *pf)
{
	int x;
	int y;
	printf("%d/%d\n", x = (*pf).num, y = (*pf).den);
}

/* Return the greatest common divisor of integers a and b; 
   i.e., return the largest positive integer that evenly divides 
   both values.
*/
int gcd(int a, int b)
{
	int x = abs(b);
	int y = abs(a);
	int z;
	z = y % x;
	while(z != 0){
		y = x;
		x = z;
		z = y % x;
		}
	return x;


}

/* Convert the fraction pointed to by pf to reduced form.

   This means that:
   (1) if the numerator is equal to 0 the denominator is always 1.
   (2) if the numerator is not equal to 0 the denominator is always
       positive, and the numerator and denominator have no common
       divisors other than 1.

   In other words,
   (1) if the numerator is 0 the denominator is always changed to 1.
   (2) if the numerator and denominator are both negative, both values
       are made positive, or if the numerator is positive and the 
       denominator is negative, the numerator is made negative and the 
       denominator is made positive.
   (3) the numerator and denominator are both divided by their greatest
       common divisor. 
*/
void reduce(fraction_t *pf)
{
	int ReducingFactor;
	int x = (*pf).num;
	int y = (*pf).den;
	if (x < 0 && y < 0){
		x = abs(x);
		y = abs(y);
		}
	else if (y < 0){
		x = -1 * x;
		y = abs(y);
		}
	else if (x == 0){
		y = 1;
		}
	else if (x != 0){
		y = abs(y);
		}
	ReducingFactor = gcd(x, y);
	x = x / ReducingFactor;
	y = y / ReducingFactor;
    *pf = (fraction_t) {x, y};

}

/* Initialize the fraction pointed to by new_fraction 
   with numerator a and denominator b.
   Print an error message and terminate the calling program via exit()
   if the denominator is 0.
   The fraction returned by this function is always in reduced form
   (see documentation for reduce).
*/
void make_fraction(int a, int b, fraction_t *new_fraction)
{
	(*new_fraction).num = a;
	(*new_fraction).den = b;
	if (b != 0){
		reduce(new_fraction);
	}
	else {
		printf("ERROR.");
		exit(0);
	}

}


/* Initialize the fraction pointed to by sum with the sum of 
   the fractions pointed to by pf1 and pf2.
   The fraction created by this function is always in reduced form
   (see documentation for reduce).
*/
void add_fractions(const fraction_t *pf1, const fraction_t *pf2, fraction_t *sum)
{
	(*sum).num = (((*pf1).num * (*pf2).den) + ((*pf1).den * (*pf2).num));
	(*sum).den = ((*pf1).den * (*pf2).den);
	reduce(sum);
}

/* Initialize the fraction pointed to by product with the product of 
   the fractions pointed to by pf1 and pf2.
   The fraction created by this function is always in reduced form
   (see documentation for reduce).
*/
void multiply_fractions(const fraction_t *pf1, const fraction_t *pf2, 
	                    fraction_t *product)
{
	(*product).num = ((*pf1).num * (*pf2).num);
	(*product).den = ((*pf1).den * (*pf2).den);
	reduce(product);
}
