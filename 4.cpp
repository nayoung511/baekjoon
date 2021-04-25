#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

#define MAX 1000001

using namespace std;

int N, d;

string S;

int SA[MAX];
int LCP[MAX];

int group[MAX];

bool cmp(int i, int j) {
  if(group[i] != group[j]) return group[i] < group[j];

  i += d;
  j += d;
  return (i < N && j < N) ? (group[i] < group[j]) : (i > j);
}

void constructSA() {
  for(int i=0; i<N; i++) {
    SA[i] = i;
    group[i] = S[i];
  }

  for(d=1; ;d*=2) {
    sort(SA, SA+N, cmp);
    int newGroup[MAX];

    for(int i=0; i<N-1; i++) {
      newGroup[i+1] = newGroup[i] + cmp(SA[i], SA[i+1]);
    }

    for(int i=0; i<N; i++) {
      group[SA[i]] = newGroup[i];
    }

    if(newGroup[N-1] == N-1) break;
  }
}

void getLCP()
{
  for(int i=0, k=0; i<N; i++, k = max(k-1, 0)) {
    if(group[i] == N-1) continue;

    for(int j=SA[group[i]+1]; S[i+k] == S[j+k]; k++);

    LCP[group[i]] = k;
  }
}

int main()
{

    cin >> S;
    N = S.size();

    constructSA();
    getLCP();


    long long ret = 0;
    for(int i=0; i<N-1; i++) {
        ret += N-SA[i]-LCP[i];
    }

    ret += N-SA[N-1];

    printf("%lld\n", ret);

  return 0;
}