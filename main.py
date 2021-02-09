from matplotlib import pyplot as plt
import numpy as np
class Polynome :
    def __init__(self,coeffs:list,degres:list):
        """
        Inputs: <list> of the coefficients
        <list> of the degrees
        
        """
        # Normalize to help for the sum
        i=0
        while coeffs[i]==0:
            coeffs.pop(i)
            i+=1
        while len(coeffs)<len(degres): degres.pop(0)
        while len(degres)<len(coeffs): coeffs.pop(0)
        self.coeffs,self.degres=coeffs,degres
    def __repr__(self):
        """
        Return x*coeff**degres+ ... for each degrees
        """
        toReturn=""
        for i in range(len(self.degres)):
            if i==0 :toReturn += f"{self.coeffs[i]}*(x)**{self.degres[i]}"
            else:toReturn += f"+ {self.coeffs[i]}*(x)**{self.degres[i]}"
        return toReturn
    def __add__(self,other):
        """
        Adding 2 polynomes
        """
        # Check if they got the same size
        if len(self.coeffs)<len(other.coeffs):degres=other.degres
        else:degres=self.degres
        while len(self.coeffs)<len(other.coeffs):
            self.coeffs.insert(0,0)
        while len(other.coeffs)<len(self.coeffs):other.coeffs.insert(0,0)
        #Adding coefficients together
        coeffs=[]
        for i in range(len(self.coeffs)):
            coeffs+=[self.coeffs[i]+other.coeffs[i]]
        return Polynome(coeffs,degres) #We return a new polynome with the new coefficients and degrees
    def calcul(self,x:float):
        """
        Return the value of the polynome at x = <x:float>
        """
        calcule=str(self).replace('x',str(x))
        return eval(calcule)
    def trace(self):
        """
        Plot the polynome using matplotlib
        """
        #X=[i for i in range(-5,5)]
        X=list(np.linspace(-5,5,100))
        Y=list(map(lambda x : self.calcul(x),X))
        plt.plot(X,Y)
        plt.title(str(self))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()
