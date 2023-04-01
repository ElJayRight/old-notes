Given two files, source.py and output.txt

Looking at the source file, each character is being encrypted one at a time with the same key. This means you can do a frequency attack as each letter will map to the same hash.

Creating a python program to map the hashes to chars.
```python
alpha = 'qwertyuiopasdfghjklzxcvbnm1234'
list = []
for line in open("output.txt",'r'):
    list.append(line.strip())
sets = set(list)
list = ' '.join(list)
for i,hash in enumerate(sets):
    print(i)
    list = list.replace(hash,alpha[i])
print(list.replace(' ',''))
```

For now it will be random but we have to include ` _{}` (including the space at the start).

Changing the most common letter to a space gives this output:
```
uvfidfa2p tatkpbxb xb ntbfy la hsf ut2h hsth xa tap 4xqfa bhvfh2s lu jvxhhfa kta4dt4f 2fvhtxa kfhhfvb tay 2lcnxathxlab lu kfhhfvb l22dv jxhs qtvpxa4 uvfidfa2xfb clvflqfv hsfvf xb t 2stvt2hfvxbhx2 yxbhvxndhxla lu kfhhfvb hsth xb vld4skp hsf btcf ulv tkclbh tkk btczkfb lu hsth kta4dt4f xa 2vpzhtatkpbxb uvfidfa2p tatkpbxb tkbl walja tb 2ldahxa4 kfhhfvb xb hsf bhdyp lu hsf uvfidfa2p lu kfhhfvb lv 4vldzb lu kfhhfvb xa t 2xzsfvhfoh hsf cfhsly xb dbfy tb ta txy hl nvftwxa4 2ktbbx2tk 2xzsfvb uvfidfa2p tatkpbxb vfidxvfb lakp t ntbx2 dayfvbhtayxa4 lu hsf bhthxbhx2b lu hsf zktxahfoh kta4dt4f tay blcf zvlnkfc blkqxa4 bwxkkb tay xu zfvulvcfy np stay hlkfvta2f ulv fohfabxqf kfhhfv nllwwffzxa4 ydvxa4 jlvky jtv xx nlhs hsf nvxhxbs tay hsf tcfvx2tab vf2vdxhfy 2lyfnvftwfvb np zkt2xa4 2vlbbjlvy zdggkfb xa ctrlv afjbztzfvb tay vdaaxa4 2lahfbhb ulv jsl 2ldky blkqf hsfc hsf utbhfbh bfqfvtk lu hsf 2xzsfvb dbfy np hsf toxb zljfvb jfvf nvftwtnkf dbxa4 uvfidfa2p tatkpbxb ulv fotczkf blcf lu hsf 2labdktv 2xzsfvb dbfy np hsf rtztafbf cf2stax2tk cfhslyb lu kfhhfv 2ldahxa4 tay bhthxbhx2tk tatkpbxb 4fafvtkkp shn1tebxczkfebdnbhxhdhxlaexbejftwm 2tvy hpzf ct2sxafvp jfvf uxvbh dbfy xa jlvky jtv xx zlbbxnkp np hsf db tvcpb bxb hlytp hsf stvy jlvw lu kfhhfv 2ldahxa4 tay tatkpbxb stb nffa vfzkt2fy np 2lczdhfv bluhjtvf jsx2s 2ta 2tvvp ldh bd2s tatkpbxb xa bf2layb jxhs clyfva 2lczdhxa4 zljfv 2ktbbx2tk 2xzsfvb tvf dakxwfkp hl zvlqxyf tap vftk zvlhf2hxla ulv 2lauxyfahxtk ytht zdggkf zdggkf zdggkf
```

Passing this to quipquip gives a very close solution
```
frequen2y analysis is based on the fa2t that in any 4iven stret2h of written lan4ua4e 2ertain letters and 2ombinations of letters o22ur with varyin4 frequen2ies moreover there is a 2hara2teristi2 distribution of letters that is rou4hly the same for almost all samples of that lan4ua4e in 2ryptanalysis frequen2y analysis also known as 2ountin4 letters is the study of the frequen2y of letters or 4roups of letters in a 2iphertext the method is used as an aid to breakin4 2lassi2al 2iphers frequen2y analysis requires only a basi2 understandin4 of the statisti2s of the plaintext lan4ua4e and some problem solvin4 skills and if performed by hand toleran2e for extensive letter bookkeepin4 durin4 world war ii both the british and the ameri2ans re2ruited 2odebreakers by pla2in4 2rossword puzzles in major newspapers and runnin4 2ontests for who 2ould solve them the fastest several of the 2iphers used by the axis powers were breakable usin4 frequen2y analysis for example some of the 2onsular 2iphers used by the japanese me2hani2al methods of letter 2ountin4 and statisti2al analysis 4enerally htb1acsimplecsubstitutionciscweakg 2ard type ma2hinery were first used in world war ii possibly by the us armys sis today the hard work of letter 2ountin4 and analysis has been repla2ed by 2omputer software whi2h 2an 2arry out su2h analysis in se2onds with modern 2omputin4 power 2lassi2al 2iphers are unlikely to provide any real prote2tion for 2onfidential data puzzle puzzle puzzle
```

This will map to the flag:
```
htb1acsimplecsubstitutionciscweakg
```
swapping: `1:{ g:} c:_`
gives 
```
HTB{a_simple_substitution_is_weak}
```

Which is the flag.