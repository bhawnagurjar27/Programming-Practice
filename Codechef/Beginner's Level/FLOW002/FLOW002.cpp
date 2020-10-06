#include <iostream> 
using namespace std;

int main() {
	
	int number_of_testcases;
	scanf("%d", &number_of_testcases);
	
	while (number_of_testcases--) {
		                                     // Read the input
		int A, B;
		scanf("%d %d", &A, &B);

		
		int remainder = A % B;
		printf("%d\n", remainder);
	}

	return 0;
}
