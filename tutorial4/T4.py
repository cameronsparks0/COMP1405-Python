import helper

def count_vowels(s:str) -> int:
    flag=0
    for x in s:
        if(helper.vowel_check(x)):
            flag = flag + 1
    return flag

def dataSlice(d:str):
    day = d[0:2]
    month = d[3:5]
    year = d[6:11]

    print(month+"/"+day+"/"+year)
    print(year+"/"+month+"/"+day)
    print(day+"-"+month+"-"+d[8:11])

def dataSplit(d:str):
    date = list(d.split("/"))

    print("/".join([date[1],date[0],date[2]]))
    print("/".join([date[2],date[0],date[1]]))
    print("-".join([date[0],date[1],date[2][2]+date[2][3]]))

def dataFormat(d:str):
    import datetime
    date = list(d.split("/"))
    d = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
    print(f'{d:%A,%B %d,%Y}')
    print(f'{d:%Y/%m/%d}')
    print(f'{d:%d-%m-%C (%b)}')

def number_of_hits(target:str, word:str) -> int:
    x = 0
    length = len(target)
    storage = 0
    z=0
    temp = ""
    while(x<len(word)-1):
        if(x+(length-1)>len(word)-1):
            return storage
        else:
            z=0
            temp=""
            while(z<length):
                temp = temp + word[x+z]
                z = z + 1
            if(target == temp):
                storage = storage + 1
            
        x = x + 1
    return storage


def main():
    print(count_vowels(input("Please enter a string: ")))
    dataSlice("27/02/2003")
    dataSplit("27/02/2003")
    dataFormat("14/10/2020")
    print(number_of_hits("qq","qqqq"))

if __name__=="__main__":
    main()