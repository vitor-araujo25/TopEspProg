#include <math.h>
#include <stdio.h>
#include <algorithm>

double Solve(long long n, long long p) {
    long long i, denominator = 1, max_element;
    double sum;
    sum = 0;
    max_element = std::max({p,n-p}); // p>(n-p)?p:n-p;
    for(i = max_element+1; i<=n; i++) {
        sum += log10((double)i/(double)denominator);
        denominator++;
    }
    return floor(sum) + 1;
}

int main() {
    long long n, p;
	while(scanf("%lld%lld",&n,&p) == 2) {
		if(n == p) { 
            printf("1\n");
            continue; 
        }
        if(p == 1 or p == n-1) { 
            printf("%.lf\n", floor(log10(n)) + 1); 
            continue;
        }
		
        printf("%.lf\n",Solve(n,p));
	}
	return 0;
}

