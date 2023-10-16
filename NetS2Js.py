import glob

files = (glob.glob("Source/*"))
for file in files:
    if(file.find("donedb_")==0):
        continue
    fh = open(file,"r")
    long = len(fh.readlines())
    fh = open(file,"r")
    fw = open("Result/"+file[7:]+".txt","w")
    fw.write("[")
    for i in range(long-1):
        ligne = fh.readline()
        indx = ligne.split()
        print(indx)
        try:
            ch ="{" + f'"domain":"{indx[0]}","expirationDate":{indx[4]},"httpOnly":{indx[1].lower()},"name":"{indx[5]}","path":"{indx[2]}","secure":{indx[3].lower()},"value":"{indx[6]}"'+"},"
        except:
            print(file)
        fw.write(ch)
    ligne = fh.readline()
    indx = ligne.split()
    print(indx)
    ch ="{" + f'"domain":"{indx[0]}","expirationDate":{indx[4]},"httpOnly":{indx[1].lower()},"name":"{indx[5]}","path":"{indx[2]}","secure":{indx[3].lower()},"value":"{indx[6]}"'+"}]"
    fw.write(ch)
