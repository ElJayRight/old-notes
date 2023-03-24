Given a ps1 script

# Solution
reading the ps1 file:
```bash
cat cradle.ps1
```
Shows an obfuscated string in the ps1 script.
```ps1
$f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}'
```

Copying it to python then printing it out.
```python
>>> f = 'H' + 'T' + 'B' + '{p0w3rs' + 'h3ll' + '_Cr4d' + 'l3s_c4n_g3t' + '_th' + '3_j0b_d' + '0n3}'
>>> f
'HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}'
```
