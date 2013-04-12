# hcut

Cutter for text files with header.


## Install
Current version is 0.1.3. 

It is available from PyPI.
```
$ sudo pip install hcut
```
or
```
$ sudo easy_install hcut
```


## Usage
```
usage: hcut [-h] [-f FIELD] [-d DELIMITER] [--header] [--version]
            [file [file ...]]

hcut

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  -f FIELD, --field FIELD
  -d DELIMITER, --delimiter DELIMITER
  --header
  --version             show program's version number and exit
```

## Example

Test data
```
$ cat a.txt
USER_ID NAME    AGE
1       Sato    10
2       Suzuki  30
3       Abe     20
```
```
$ cat b.txt
USER_ID NAME    AGE
4       Takahashi       40
5       Ito     50
```

From stdin.
```
$ cat a.txt | hcut --header -f USER_ID -f NAME
USER_ID NAME
1       Sato
2       Suzuki
3       Abe
```

With file arguments.
```
$ hcut -f USER_ID -f NAME a.txt b.txt
1       Sato
2       Suzuki
3       Abe
4       Takahashi
5       Ito
```
With the header.
```
$ hcut --header -f USER_ID -f NAME a.txt b.txt
USER_ID NAME
1       Sato
2       Suzuki
3       Abe
4       Takahashi
5       Ito
```
