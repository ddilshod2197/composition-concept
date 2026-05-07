class Avto:
    def __init__(self, rang, model):
        self.rang = rang
        self.model = model

class Motor:
    def __init__(self, hajm, silindr_soni):
        self.hajm = hajm
        self.silindr_soni = silindr_soni

class Kompozitsiya:
    def __init__(self, avto, motor):
        self.avto = avto
        self.motor = motor

avto = Avto("Qizil", "Toyota")
motor = Motor("2.5", 4)
kompozitsiya = Kompozitsiya(avto, motor)

print(kompozitsiya.avto.rang)  # Qizil
print(kompozitsiya.avto.model)  # Toyota
print(kompozitsiya.motor.hajm)  # 2.5
print(kompozitsiya.motor.silindr_soni)  # 4
```

Composition nima?.
