class dad:
    def phone(self,SAMsung):
        self.brand = SAMsung
        print("Dad phone",self.brand)

class mom:
    def mom_great(self):
        print('Happy day')

class son(dad,mom): #multip inheritance
    def son_phone(self):
        print("Son's Mobile")

rohit = son()
rohit.phone("Sam")                # calling dad's method to set brand
rohit.mom_great()          
    # ✅ now works

