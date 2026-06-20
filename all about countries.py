class India:
    def capital (self):
        print("New Dehli is the Capital of India")
    
    def language (self):
        print("Hindi is the primary language of India")

    def type (self):
        print("India is a Developing Country")

class USA:
    def capital (self):
        print("\nWashington, D.C. is the Capital of the USA")
    
    def language (self):
        print("English is the primary language of the USA")

    def type (self):
        print("USA is a Developed Country")

class Canada:
    def capital (self):
        print("\nOttawa is the Capital of Canada")
    
    def language (self):
        print("English and French are the primary languages of Canada")

    def type (self):
        print("Canada is a Developed Country")
    
indobj = India()
usaobj = USA()
canobj = Canada()

for country in (indobj, usaobj, canobj):
    country.capital()
    country.language()
    country.type()