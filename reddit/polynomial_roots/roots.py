import re

#splits an equation of the form ax^b+cx+d
#all exponents and coefficients must be integers
#exponents must be 0 <= exp <= 9
#Returns a list of tuples
def split_eq(eq):
    a = re.compile(r'([-+]?\d*x?(?:\^?[\d])?)')
    b = re.compile(r'x?[\^]?')

    eq = re.split(a, eq)
    eq = filter(None, eq)
    terms = []
    for elem in eq:
        cof = 1
        if 'x' in elem:
            exp = 1
        else:
            exp = 0
        elem = re.split(b, elem)
        if len(elem) == 1:
            elem.append(None)
        if elem[0]:
            cof = int(elem[0])
        if elem[1]:
            exp = int(elem[1])
        terms.append((cof,exp))
    return terms

#Evaluates the term list with the given x value
def eval_eq(x, terms):
    result = 0.
    for term in terms:
        result += term[0]*(x**term[1])
    return result

#Evaluates the derivative of a list of terms
def deriv_eq(terms):
    deriv = []
    for term in terms:
        if term[1] == 0:
            continue
        deriv.append((term[0]*term[1],term[1]-1))
    return deriv

#Newton's Method
def newton_method(eq, x_0=5,tol=.000001):
    eq = split_eq(eq)
    deriv = deriv_eq(eq)
    if eval_eq(x_0,eq) == 0:
        return x_0
    for i in xrange(0,100000000):
        x_1 = x_0 - (eval_eq(x_0,eq)/eval_eq(x_0,deriv))
        if abs(x_1-x_0) < tol:
            return x_1
        else:
            x_0 = x_1

while True:
    eq = raw_input()
    if not eq: break
    print "Root of %s : %.5g" % (eq,newton_method(eq))
