class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi_n = (p - 1) * (q - 1)
        self.e = e
        self.d = self.compute_modular_inverse(e, self.phi_n)
    
    def modular_inverse(self, a, m):
        #Euclidean Algorithm 4 modular inverse
        g, x, y = self.extended_gcd(a, m)
        if g != 1:
            raise ValueError
        return x % m
    
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, x, y = self.extended_gcd(b % a, a)
            return g, y - (b // a) * x, x
    
    def encrypt(self, m):
        return pow(m, self.e, self.n)
    
    def decrypt(self, c):
        return pow(c, self.d, self.n)
