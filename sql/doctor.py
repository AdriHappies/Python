class Doctor:
    hoscod = 0
    docnum = 0
    ape = ""
    espe = ""
    sal = 0

    def __str__(self):
        return (str(self.hoscod) + " - " + str(self.docnum) + " - " 
        + self.ape + " - " + self.espe + " - " + str(self.sal))