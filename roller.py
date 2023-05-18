
class Eroller:
    def __init__(self, marka, seb, telj) -> None:
        self.marka= marka
        self.maxseb= int(seb)
        self.teljesitmeny = int(telj)


    def ToString(self):
        kimenet = f"A roller márkája: {self.marka}\n"
        kimenet += f"Maximális sebessége: {self.maxseb}\n"
        kimenet += f"Teljesítménye: {self.teljesitmeny} W"
        return kimenet

    

ujRoller1 = Eroller("Akai F10",25,250)
print(ujRoller1.ToString())


ujRoller2 = Eroller("xiaomi",40,350)
print(ujRoller2.ToString())


ujRoller3 = Eroller("Bugatti",45,400)
print(ujRoller3.ToString())


ujRoller1.marka
print("Az új roller márkájának neve: {ujRoller1.marka}")

ujRoller2.marka
print("Az új roller márkájának neve:  {ujRoller2.marka}")

ujRoller3.marka
print("Az új roller márkájának neve:  {ujRoller3.marka}")