class dad:
    def phone(self):
        self.brand = "Redmi"
        print("Dad phone")

class son(dad):
    def son_phone(self):
        print("Son's Mobile")

rohit = son()
rohit.phone()          # calling dad's method to set brand
print(rohit.brand)     # ✅ now works
# rohit.son_phone()
