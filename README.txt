README of the CIBB dataset.

1.Files in this directory:

- README.txt: This file.

- filter-trig-pairs.py: The python script for automatically separating translations triggering or not triggering the blacklist. (Need 'nltk' package to run)

- idiom_blacklist.blacklist.en.txt: The blacklist for each Chinese source sentence.

- idiom_blacklist.src.zh.txt: Chinese source sentences.

- idiom_blacklist.ref.en.txt: Reference English translations for each Chinese source sentence.

- list_idiom_blacklist.txt: The idiom list. Every 5 lines describe an idiom. The format is like the following:
The Chinese idiom
Frequency in the training data
English translation
Blacklist
(blank line)

2. How to execute the evaluation:
(1) Translate all the Chinese source sentences using your MT system. Put all the translations in a file named 'idiom_blacklist.trans.en.txt' under this directory, one translation in a line, just like in 'idiom_blacklist.ref.en.txt'.
(2) Run the script 'filter-trig-pairs.py'.
(3) All the translations triggering the blacklist will be put into file 'idiom_blacklist.trig.pairs.txt', while those not triggering the blacklist will be put into 'idiom_blacklist.nontrig.pairs.txt'. The result (how many triggered, how many not) will be printed on the shell.