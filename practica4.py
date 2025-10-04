from datetime import date, datetime
from abc import ABC, abstractmethod   # para clases y métodos abstractos

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

    def _calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self._fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day)
        )
        return edad

    def obtener_edad(self):
        return self._calcular_edad()


class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_interes=0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se depositaron {monto} a la cuenta de {self._nombre_titular}. Saldo actual: {self._saldo}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def extraer(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se extrajeron {monto} de la cuenta de {self._nombre_titular}. Saldo actual: {self._saldo}")
        else:
            print("Fondos insuficientes.")

    def calcular_interes(self):
        interes = self._saldo * self._tasa_interes
        print(f"El interés generado es de: {interes}")
        return interes







