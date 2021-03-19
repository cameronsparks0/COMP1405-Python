def pair(strand : str) -> str:
    rPair = ""
    strand = strand.upper()
    for x in strand:
        if(x=="A"):
            rPair = rPair + "T"
        elif(x=="T"):
            rPair = rPair + "A"
        elif(x=="C"):
            rPair = rPair + "G"
        elif(x=="G"):
            rPair = rPair + "C"
    return rPair

def compress(strand : str) -> str:
    x=0
    strand = strand.upper()
    aCounter = 0
    tCounter = 0
    cCounter = 0
    gCounter = 0
    compressedStrand =""
    while x < len(strand):
        if strand[x] == "A":
            while strand[x]=="A":
                aCounter = aCounter+1
                if(x<(len(strand))-1):
                    x = x+1
                else:
                    x= x+1
                    break
            if(aCounter>1):
                compressedStrand = compressedStrand + str(aCounter)+ "A"
            else:
                compressedStrand = compressedStrand + "A"
            aCounter=0

        elif strand[x] == "T":
            while strand[x]=="T":
                tCounter = tCounter+1
                if(x<(len(strand))-1):
                    x = x+1
                else:
                    x= x+1
                    break
            if(tCounter>1):
                compressedStrand = compressedStrand + str(tCounter)+ "T"
            else:
                compressedStrand = compressedStrand + "T"
            tCounter=0
        
        elif strand[x] == "C":
            while strand[x]=="C":
                cCounter = cCounter+1
                if(x<(len(strand))-1):
                    x = x+1
                else:
                    x= x+1
                    break
            if(cCounter>1):
                compressedStrand = compressedStrand + str(cCounter)+ "C"
            else:
                compressedStrand = compressedStrand + "C"
            cCounter=0
        
        elif strand[x] == "G":
            while strand[x]=="G":
                gCounter = gCounter+1
                if(x<(len(strand))-1):
                    x = x+1
                else:
                    x= x+1
                    break
            if(gCounter>1):
                compressedStrand = compressedStrand + str(gCounter)+ "G"
            else:
                compressedStrand = compressedStrand + "G"
            gCounter=0

        if(x==(len(strand))):
            return compressedStrand

def expand(compressedStrand : str) -> str:
    compressedStrand = compressedStrand.upper()
    numbStore = ""
    compressedDna = ""
    for x in compressedStrand:
        if(x.isdigit()):
            numbStore = numbStore+x
        else:
            if(numbStore==""):
                compressedDna = compressedDna + x
            else:
                compressedDna = compressedDna + int(numbStore)*x
            numbStore = ""
    return compressedDna


        



print(pair("TGACCCC"))
print(compress("tataaaccgggggggggggggggggggggggggg"))
print(expand("2g10aagt100t"))