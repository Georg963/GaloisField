from .modPolys import modularPolynome
from .unicodes import exponents, alpha
from .alpha import alpha1

class gf:

    def __init__(self, gf):
        self.gf = gf
        self.modPol = modularPolynome[self.gf - 2]

    def __str__(self):
        return 'GF(2' + ''.join(exponents[int(i)] for i in str(self.gf)) + ')'
    
    def modPol_vr(self):
        return self.modPol

    def modPol_pr(self):
        alphas = []
        for ind, val in enumerate(reversed(self.modPol)):
            if val == '1':
                if ind <= 9:
                    alphas.append(alpha + exponents[ind])
                else:
                    alphas.append(alpha + ''.join(exponents[int(j)] for j in str(ind)))
        
        return ' + '.join(reversed(alphas))
    
    def getElements(self):
        startNum = 1
        alphas_vr = []

        for i in range(0, (2**self.gf)-1):
            if startNum < (2**self.gf):
                alphas_vr.append(startNum)
            else:
                startNum = startNum ^ int(modularPolynome[self.gf - 2], 2)
                alphas_vr.append(startNum)
            startNum = startNum << 1
        
        for i in range(len(alphas_vr)):
            value = bin(alphas_vr[i])[2:]
            alphas_vr[i] = ''.join('0' for j in range(len(value), self.gf)) + value
        
        alphas_vr = [alpha1(alphas_vr, i) for i in range(len(alphas_vr))]
        return alphas_vr