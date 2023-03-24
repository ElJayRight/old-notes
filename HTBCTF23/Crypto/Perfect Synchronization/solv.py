'''
alpha = 'qwertyuiopasdfghjklzxcvbnm12345'
list = []
for line in open("output.txt",'r'):
    list.append(line.strip())
sets = set(list)
list = ' '.join(list)
for i,hash in enumerate(sets):
    print(i)
    list = list.replace(hash,alpha[i])
print(list.replace(' ',''))
'''
dump = 'uvfidfa2p tatkpbxb xb ntbfy la hsf ut2h hsth xa tap 4xqfa bhvfh2s lu jvxhhfa kta4dt4f 2fvhtxa kfhhfvb tay 2lcnxathxlab lu kfhhfvb l22dv jxhs qtvpxa4 uvfidfa2xfb clvflqfv hsfvf xb t 2stvt2hfvxbhx2 yxbhvxndhxla lu kfhhfvb hsth xb vld4skp hsf btcf ulv tkclbh tkk btczkfb lu hsth kta4dt4f xa 2vpzhtatkpbxb uvfidfa2p tatkpbxb tkbl walja tb 2ldahxa4 kfhhfvb xb hsf bhdyp lu hsf uvfidfa2p lu kfhhfvb lv 4vldzb lu kfhhfvb xa t 2xzsfvhfoh hsf cfhsly xb dbfy tb ta txy hl nvftwxa4 2ktbbx2tk 2xzsfvb uvfidfa2p tatkpbxb vfidxvfb lakp t ntbx2 dayfvbhtayxa4 lu hsf bhthxbhx2b lu hsf zktxahfoh kta4dt4f tay blcf zvlnkfc blkqxa4 bwxkkb tay xu zfvulvcfy np stay hlkfvta2f ulv fohfabxqf kfhhfv nllwwffzxa4 ydvxa4 jlvky jtv xx nlhs hsf nvxhxbs tay hsf tcfvx2tab vf2vdxhfy 2lyfnvftwfvb np zkt2xa4 2vlbbjlvy zdggkfb xa ctrlv afjbztzfvb tay vdaaxa4 2lahfbhb ulv jsl 2ldky blkqf hsfc hsf utbhfbh bfqfvtk lu hsf 2xzsfvb dbfy np hsf toxb zljfvb jfvf nvftwtnkf dbxa4 uvfidfa2p tatkpbxb ulv fotczkf blcf lu hsf 2labdktv 2xzsfvb dbfy np hsf rtztafbf cf2stax2tk cfhslyb lu kfhhfv 2ldahxa4 tay bhthxbhx2tk tatkpbxb 4fafvtkkp shn1tebxczkfebdnbhxhdhxlaexbejftwm 2tvy hpzf ct2sxafvp jfvf uxvbh dbfy xa jlvky jtv xx zlbbxnkp np hsf db tvcpb bxb hlytp hsf stvy jlvw lu kfhhfv 2ldahxa4 tay tatkpbxb stb nffa vfzkt2fy np 2lczdhfv bluhjtvf jsx2s 2ta 2tvvp ldh bd2s tatkpbxb xa bf2layb jxhs clyfva 2lczdhxa4 zljfv 2ktbbx2tk 2xzsfvb tvf dakxwfkp hl zvlqxyf tap vftk zvlhf2hxla ulv 2lauxyfahxtk ytht zdggkf zdggkf zdggkf'
for i in set(list(dump)):
    if dump.count(i) == 230:
        print(i)