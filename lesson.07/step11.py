class Device:
    def scanning(self):
        return "Я ТОЧНО НЕ сканирую"


class Printer(Device):
    def printing(self, text):
        return f"Я печатаю: {text}"
    #
    # def scanning(self):
    #     return "Я НЕ сканирую"


class Scanner:
    def scanning(self):
        return "Я сканирую"


class MFP(Printer, Scanner):
    pass


device = MFP()
print(device.scanning())
print(device.printing("Bob 123"))
print(MFP.mro())