import glob
# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob('./'+'**/*.md', recursive=True):
     print(f'* [{filename.split("/")[-1][:-3]}]({filename.replace(" ","%20").split("/")[-1]})')