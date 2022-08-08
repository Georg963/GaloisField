from .unicodes import alpha, exponents

class alpha1():

    def __init__(self, alphas, exponent):
        self.alphas = alphas
        self.exponent = exponent
        self.alpha = "".join([i for i in self.alphas[self.exponent]])
        self.length = (2**len(self.alpha)) - 1

    def __str__(self):
        return self.alpha
    
    def __repr__(self):
        return self.alpha
    
    def getAlpha(self):
        return alpha + ''.join(exponents[int(i)] for i in str(self.exponent))
        
    def __add__(self, summand):
       return alpha1(self.alphas, self.alphas.index(''.join('0' if self.alpha[i] == summand.alpha[i] else '1' for i in range(len(self.alpha)))))

    def __neg__(self):
        return alpha1(self.alphas, (self.length - self.exponent) % self.length)

    def __mul__(self, factor):
        return alpha1(self.alphas, (self.exponent + factor.exponent) % self.length)
    
    def __truediv__(self, divisor):
        return alpha1(self.alphas, (self.exponent - divisor.exponent) % self.length)
    
    def __pow__(self, num):
        return alpha1(self.alphas, (self.exponent * num) % self.length)