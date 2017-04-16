#!/usr/bin/env python

import decimal
import math

def msqrt(n):
    if n == 0 or n == 1:
	return n

    with decimal.localcontext() as ctx:
        x, prior = decimal.Decimal(n), None
        while x != prior: 
            prior = x
            x = (x + n/x) / 2 # quadratic convergence 

    return (+x) 

decimal.getcontext().prec = 20 # desirable precision
print msqrt(338727899)
#print int(math.floor(msqrt(338727899)))
