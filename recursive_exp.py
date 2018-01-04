print 2**5

def pow(base, exp):
    """ calculate base**exp recursively """
    print "base:", base, "exp:", exp
    if exp == 0:
        return 1
    x = base*pow(base,exp-1)
    print x,
    return x

pow(2,5)
