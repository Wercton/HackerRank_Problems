#include <stdio.h>
#include <stdlib.h>


//"Hello World!" in C
void hello_world(){

	char s[100];
	scanf("%[^\n]%*c", &s);

	printf("Hello, World!\n");
	printf(s);
}


//Playing With Characters
void three_inputs_for_three_outputs(){
	char ch, s[50], sen[50];

	scanf("%c", &ch);
	scanf("%s\n", &s);
	scanf("%[^\n]%*c", &sen);

	printf("%c\n", ch);
	printf("%s\n", s);
	printf("%s\n", sen);
}


//Sum and Difference of Two Numbers
void sum_difference_int_and_float(){
	int integer1, integer2;
	float float1, float2;

	scanf("%d %d %f %f", &integer1, &integer2, &float1, &float2);

	printf("%d %d\n", integer1 + integer2, integer1 - integer2);
	printf("%.1f %.1f\n", float1 + float2, float1 - float2);
}


//Functions in C
int max_of_four(){
	int a, b, c, d, max;

	scanf("%d %d %d %d", &a, &b, &c, &d);
	max = a;
	
	if(b > max)
		max = b;
	if(c > max)
		max = c;
	if(d > max)
		max = d;

	printf("%d\n", max);
}


//Pointer in C
void update(int *a,int *b) {
    int aux=*a;
    *a = *a + *b;
    *b = aux - *b;
    if(*b<0)
        *b = *b * -1;
}


void pointers(){
	int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);
}


int main(){
	//hello_world();
	//three_inputs_for_three_outputs();
	//sum_difference_int_and_float();
	//max_of_four();
	pointers();

	return 0;
}