from rower import Rower
from samochod import Samochod

rw = Rower("Trek","MadOne",2020,"korba","czerwony","shimano",12.4,True)

print(rw.daneroweru())
print(rw.naped())

rw.set_waga_ramy(13.7)
print(rw.daneroweru())

print("______________________________________________")

sm = Samochod("Opel","Insignia",2019,"silnik diesel","czarny",2.2,212,True)
print(f"prędkość masymalna: {sm.vmax()} km/h")
print(sm.naped())
sm.set_moc(219)
print(sm.naped())
