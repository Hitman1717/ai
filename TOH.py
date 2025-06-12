def TOH(n,s,h,d):
    if(n==1):
        print("disk",n,"from ",s,"to ",d)
        return 
    TOH(n-1,s,d,h)
    print("disk",n,"from ",s,"to ",d)
    TOH(n-1,h,s,d)
    return 


# main

TOH(3,"s","h","d")