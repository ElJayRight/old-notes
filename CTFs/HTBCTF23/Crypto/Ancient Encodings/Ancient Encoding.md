Given a source and output file.

# Solution
Looking at the source file, it just seems to encoding types.

```
cat output.txt |xxd -p -r|base64 -d
```

Which gives
```
HTB{1n_y0ur_j0urn3y_y0u_wi1l_se3_th15_enc0d1ngs_ev3rywher3}
```