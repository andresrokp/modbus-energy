
def conv754toDEC(msw, lsw):
    denom = 0x800000
    mantissa = 0
    expon = 0
    for i in range(16,0,-1):
        if lsw & 1:
            mantissa += (1 / denom)
        denom = denom >> 1
        lsw = lsw >> 1
    for i in range(7,0,-1):
        if msw & 1:
            mantissa += (1 / denom)
        denom = denom >> 1
        msw = msw >> 1
    expon = (0xff & msw) - 127
    if msw & 0x100:
        sign = -1
    else:
        sign = 1
    return (sign * (1 + mantissa) * 2**expon);
