class NumeroComplejo:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag

    def __str__(self):
        # Representación en cadena del número complejo
        return f"{self.real} + {self.imag}i"

    def suma(self, otro):
        # Suma de números complejos
        real = self.real + otro.real
        imag = self.imag + otro.imag
        return NumeroComplejo(real, imag)

    def resta(self, otro):
        # Resta de números complejos
        real = self.real - otro.real
        imag = self.imag - otro.imag
        return NumeroComplejo(real, imag)

    def multiplicacion(self, otro):
        # Multiplicación de números complejos
        real = self.real * otro.real - self.imag * otro.imag
        imag = self.real * otro.imag + self.imag * otro.real
        return NumeroComplejo(real, imag)

    def division(self, otro):
        # División de números complejos
        divisor = otro.real**2 + otro.imag**2
        real = (self.real * otro.real + self.imag * otro.imag) / divisor
        imag = (self.imag * otro.real - self.real * otro.imag) / divisor
        return NumeroComplejo(real, imag)


# Ejemplo de uso:
if __name__ == "__main__":
    c1 = NumeroComplejo(3, 2)
    c2 = NumeroComplejo(1, 7)

    suma = c1.suma(c2)
    resta = c1.resta(c2)
    multiplicacion = c1.multiplicacion(c2)
    division = c1.division(c2)

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División:", division)
