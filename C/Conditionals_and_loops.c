#include <stdio.h>
#include <stdlib.h>


// Conditional Statements in C
void spelling_the_number(){
	static const char *strings[] = {"zero","one","two","three","four","five",
                               		"six","seven","eight","nine"};
	int number = 0;
	scanf("%d", &number);

	if(number >= 0 && number <= 9)
		printf("%s\n", strings[number]);
	else
		printf("Greater than 9\n");
}


// For Loop in C
void looping_the_numbers(){
	char *strings[] = {"zero","one","two","three","four","five",
                               		"six","seven","eight","nine"};
	int start, end;
	scanf("%d \n %d", &start, &end);

	for( ; start <= end; start++){
		if(start <= 9){
			printf("%s\n", strings[start]);
		}else{
			if((start % 2) == 0){
				printf("even\n");
			}else{
				printf("odd\n");
			}
		}
	}
}


// Sum of Digits of a Five Digit Number
void sum_the_digits(){
	char[100] number;
	int add=0;

	scanf("%s", &number);

	for(i = 0; i >= strlen(number); i++){
		add += int(number[i]);
	}

	printf("%d\n", add);
}


int main(){

	//spelling_the_number();
	// looping_the_numbers();
	sum_the_digits();

	return 0;
}
