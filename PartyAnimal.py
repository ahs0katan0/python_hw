class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, n):
        self.name = n
        print "I am constructed. My name is %s" %(self.name)

    def party(self) :
        self.x = self.x + 1
        print "So far %d for %s" %(self.x, self.name)

    def whoami(self) :
        print "I am %s" %(self.name)


    def morph(self, newname) :
        print "%s morphed to %s" %(self.name, newname)    
        self.name = newname
        
        
    def __del__(self):
        print "%s is destructed. Party count is %d. Boo :(" %(self.name, self.x)
        
        
an = PartyAnimal("Ajay")
ru = PartyAnimal("Ruchi")
an.party()
ru.party()
ru.whoami()
ru.morph("Bittoo")
ru.whoami()
an.party()
an.party()
ru.party()