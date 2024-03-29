def bsearch(seq,v,l,r): #binary search in python returns true if v is found in seq[l:r]
    if (r-l)==0:
        return(False)
    mid=(l+r)//2
    if (v==seq[mid]):
        return(True)
    if (v<seq[mid]):
        return(bsearch(seq,v,l,mid))
    else:
        return(bsearch(seq,v,mid+1,r))

# imp file dont modify
