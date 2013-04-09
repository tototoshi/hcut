# hcut

## Example
```
$ cat a.txt
USER_ID NAME    AGE
1       Sato    10
2       Suzuki  30
3       Abe     20
$ cat b.txt
USER_ID NAME    AGE
4       Takahashi       40
5       Ito     50
$ cat a.txt | ./hcut --header -f USER_ID -f NAME
USER_ID NAME
1       Sato
2       Suzuki
3       Abe
$ ./hcut -f USER_ID -f NAME a.txt b.txt
1       Sato
2       Suzuki
3       Abe
4       Takahashi
5       Ito
$ ./hcut --header -f USER_ID -f NAME a.txt b.txt
USER_ID NAME
1       Sato
2       Suzuki
3       Abe
4       Takahashi
5       Ito
```
