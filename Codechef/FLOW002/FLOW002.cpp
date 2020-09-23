#include <iostream> 
using namespace std;

int main() {
	
	int number_of_testcase;
	scanf("%d", &number_of_testcase);
	
	while (number_of_testcase--) {
		                                     // Read the input
		int A, B;
		scanf("%d %d", &A, &B);

		
		int remainder = A % B;
		printf("%d\n", remainder);
	}

	return 0;
}
