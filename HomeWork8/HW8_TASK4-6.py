class Store():

    def __init__(self, id, name, address, max_obj):
        self.id = id
        self.name = name
        self.address = address
        self.max_obj = max_obj
        self.equip = []

    def send_to(self, *eq):
        for el in eq:
            self.equip.append(el)
        print(self.equip)


class OfficeEquip(Store):
    def __init__(self, id, model, name):
        self.id = id
        # self.type = type
        self.model = model
        self.name = name



class Printer(OfficeEquip):
    def __init__(self, id, model, name):
        super().__init__(id, model, name)
        self.type = "Printer"


class Scanner(OfficeEquip):
    def __init__(self, id, model, name):
        super().__init__(id, model, name)
        self.type = "Scanner"


class Copier(OfficeEquip):
    def __init__(self, id, model, name):
        super().__init__(id, model, name)
        self.type = "Scanner"


store_01 = Store(1, "Store № 1", "Moscow, Teatralnaya 7", 5)
printer_01 = Printer("p1", "HP ", "LaserJet Pro M254dw")
printer_02 = Printer("p2", "HP ", "LaserJet M25")

store_01.send_to(printer_01.id, printer_02.id)
