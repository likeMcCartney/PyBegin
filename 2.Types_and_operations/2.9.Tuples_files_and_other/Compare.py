L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)       # L1 equals L2? Is the same object?

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)

S1 = 'a longer string aee;efovujpqewfomk;qewokfjp;oqewkjfm;oqewrkmf;oqewjkf'
S2 = 'a longer string aee;efovujpqewfomk;qewokfjp;oqewkjfm;oqewrkmf;oqewjkf'
print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print((L1 < L2, L1 == L2, L1 > L2))
