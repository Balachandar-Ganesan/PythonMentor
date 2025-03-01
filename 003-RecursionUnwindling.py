def WhatItDoes(n):
    if(n==0):
        return
    WhatItDoes(n-1)
    print(n)
WhatItDoes(4)
