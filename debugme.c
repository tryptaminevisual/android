//Compile me with optimization option -O0 for easy comprenhension.
#include <stdio.h>

void FunA(){
	printf("This is function A.\n");
}

void FunB(){
	printf("This is function B.\n");
}

int FunC(int p1, int p2){
	int i=0;
	i = p1+p2;
	return i;
}

int FunD(int input){
	char key[8] = {'m','O','b','I','l','e','A'};
	int enc;
	enc = input^key[0]^key[1]^key[2]^key[3]^key[4]^key[5]^key[6]^key[7];
	return enc;
}

void main(){
	int x,y;
	FunA();
	FunB();
	x = FunC(3,4);
	printf("This is function result: %d\n",x);
	while(x<100){
		y = FunD(x+y);
		x++; 	
	}
	printf("%d\n",y);
}