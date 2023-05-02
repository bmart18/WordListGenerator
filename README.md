# WordListGenerator
Simple program to create a wordlist of US 9 digit phone numbers for a given area code

---
Give the area code as a command line arguement, you can do as many as you want just add spaces between. It will make a separate list for each one

```Python areacode.py 167 463 433```

***Output: 167list.txt, 463list.txt, 433list.txt***

---
to combine all areacodes into one list add -s before adding area codes

```Python areacode.py -s 167 463 433```

***Output: 167463433list.txt***

---
Good to be used for Aircrack-ng WPA/WPA2 cracking as phone numbers are a common wifi password

Might add more list generators in the future.
