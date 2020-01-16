# Assignment 1

```bash
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson$ cd Desktop/
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ pwd
/mnt/c/Users/brcarlson/Desktop
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ pwd -P
/mnt/c/Users/brcarlson/Desktop
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ mkdir AFS505
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ cd AFS505
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ touch foo.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ ls
foo.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ mv foo.txt ..
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ ls
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ cd ..
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ rmdir AFS505/
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ cp foo.txt fooer.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ ls foo*
foo.txt  fooer.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ echo 'some text' >> foo.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ more foo.txt
some text
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ mkdir AFS505
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ pushd AFS505
/mnt/c/Users/brcarlson/Desktop/AFS505 /mnt/c/Users/brcarlson/Desktop
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ pwd
/mnt/c/Users/brcarlson/Desktop/AFS505
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ dirs
/mnt/c/Users/brcarlson/Desktop/AFS505 /mnt/c/Users/brcarlson/Desktop
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop/AFS505$ popd
/mnt/c/Users/brcarlson/Desktop
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ cat foo.txt
some text
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ echo 'some more text' >> fooer.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ cat foo.txt fooer.txt
some text
some more text
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ rm fooer.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ ls foo*
foo.txt
brcarlson@PW48-LMWC-07931:/mnt/c/Users/brcarlson/Desktop$ less foo.txt

some text
foo.txt (END)


```
