def insertion_sort(values): #From class
    for index in range(1, len(values)):
        #invariant: values[:index] is sorted

        # insert next value into sorted part
        pos = index
        while pos >= 1 and values[pos-1] > values[pos]:
            # swap values[pos-1] and values[pos]
            tmp = values[pos]
            values[pos] = values[pos-1]
            values[pos-1] = tmp
            pos -= 1
    return values

def bucket_sort(numberList:list)->list:
    N = len(numberList)
    mainBucketList = []
    returnList = []
    for counter in range(1,N+1):
        mainBucketList.append([])
    for counter in numberList:
        indexPosition = int((counter*N))
        mainBucketList[indexPosition].append(counter)
    for counter in range(0,N):
        returnList.extend(insertion_sort(mainBucketList[counter]))
    return returnList

def main():
    S = [0.5429,0.9384,0.1253,0.4523,0.2341,0.2948,0.682,0.7123]
    #sortedS=bucket_sort(S)
    #print(S)
    #print(sortedS)
if __name__ == "__main__":
    main()