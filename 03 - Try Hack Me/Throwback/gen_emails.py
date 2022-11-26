with open("new-emails.txt",'r') as file, open("new-email-names.txt",'w') as out:
    for i in file:
        i = i.strip()+"@TBHSecurity.com\n"
        out.write("ESM-"+i)
        out.write("FIN-"+i)
        out.write("HRE-"+i)
        out.write("ITS-"+i)
        out.write("SEC-"+i)
    out.close()