/* Tauheed Alamgir 101194927 */

/* SYSC 2006 Lab 3. 

 * Incomplete implementations of the functions that will be coded during the lab.
 */

#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#include "exercises.h"

/* Exercise 1. */

/* Return the average magnitude of the n doubles in x[]. 
 * This function assumes that parameter n is >= 1.
 */
double avg_magnitude(double x[], double n)
{
	double total = 0;
	int i;
	for (i = 0; i < n; i = i + 1){
		total = total + fabs(x[i]);
	}
	double avgmag = total / i;
    return avgmag;
}

/* Exercise 2. */

/* Return the average power of the n doubles in x[].
 * This function assumes that parameter n is >= 1.
 */
double avg_power(double x[], double n)
{
	double total = 0;
	int i;
	for (i = 0; i < n; i = i + 1){
		total = total + pow(x[i], 2);
	}
    return total/n;
}

/* Exercise 3. */

/* Return the largest of the n doubles in arr[]. 
 * This function assumes that parameter n is >= 1.
 */
double max(double arr[], int n)
{
	double maxi = arr[0];
	int i;
	for (i = 0; i < n; i = i + 1){
		if (arr[i] > maxi)
			maxi = arr[i];
	}
    return maxi;
}

/* Exercise 4. */

/* Return the smallest of the n doubles in arr[]. 
 * This function assumes that parameter n is >= 1.
 */
double min(double arr[], int n)
{
	double mini = arr[0];
	int i;
	for (i = 0; i < n; i = i + 1){
		if (arr[i] < mini)
			mini = arr[i];
	}
    return mini;
}

/* Exercise 5. */

/* Normalize the n doubles in x[]. 
 * This function assumes that parameter n is >= 2, and that at least
 * two of the values in x[] are different.
 */
void normalize(double x[], int n)
{
	double maxi = max(x, n);
	double mini = min(x, n);
	int i;
	for (i = 0; i < n; i = i + 1){
		x[i] = ((x[i] - mini) / (maxi - mini));
	} 
}




