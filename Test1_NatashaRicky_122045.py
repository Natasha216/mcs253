

#Question 1
userinput=float(input("What is the given interest rate? :"))    #0.1
userinput1=int(input("How many years does it take for the loan to be repaid? :"))   #2
userinput2=int(input("How much was loaned from the bank? :")) #30,000


class FinancialFun:
    def __init__(self,r,t,pv):
        self.r=r
        self.t=t
        self.pv=pv
    def rate(self):
        rate=((self.r/100)/12)
        print(rate)
        
    def timeperiod(self):
        timeperiod= self.t*12
        print(timeperiod)
        
    
class PMT (FinancialFun):
    def calcPMT(self):
        
        self.r=userinput
        self.t=userinput1
        self.pv=userinput2
        pmt= (self.pv * self.rate()) / (1 - (1 + self.rate())**(-self.timeperiod()))
        myrate= self.rate()
        mytimeperiod=self.timeperiod()
        
        print(pmt)
      


loan1=PMT(userinput,userinput1,userinput2)
loan1.calcPMT()

#Answer = K8.33 monthly

        
#Question 2.
#1 No, there is no restriction on printing the attributes, they were not private.

#2 No, a function is not created outside of the classes, however an object  was created outside of the clsses therefore it is not a polymorphism.

#3 They were inherited to the child class and then converted to userinputs, as the values will be given by the users.






       
#Question 3

userinput=int(input("enter value of a shorter side a: \n")) #2
userinput1=int(input("enter value of a shorter side b: \n")) #3

hypotenuse= lambda x,y: x**2 + y**2
print(hypotenuse(userinput,userinput1))

#Answer = squareroot of 13

