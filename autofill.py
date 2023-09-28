
def search(InputStr,a):
    l=[]
    for i in a:
        if len(l)<3:
            if str(i).lower().startswith(InputStr.lower()):
                l.append(i)
            else:
                continue
    return l
