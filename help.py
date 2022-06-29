

def sort(a):

    for i in range(0,5):
        for j in range(i+1,5):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a