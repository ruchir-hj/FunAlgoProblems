# solution recursive
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1 / self.powRecu(x, -n)
        
        return self.powRecu(x, n)
    
    def powRecu(self, x, n):
        if n == 0:
            return 1.0
        
        if n % 2 == 0:
            return self.powRecu(x * x, n / 2)
        else:
            return x * self.powRecu(x * x, n / 2)

# solution iterative
# solution 1
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            if n % 2 == 0:
                r = self.pow(x, n / 2)
                return r * r
            else:
                r = self.pow(x, (n - 1) / 2)
                return r * r * x
                
# solution 2
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            if n % 2 == 0:
                return self.pow(x * x, n / 2)
            else:
                return self.pow(x * x, (n - 1) / 2) * x

# solution 3
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            return self.pow(x, n / 2) * self.pow(x, n - n / 2)
          
