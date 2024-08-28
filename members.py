from abc import ABC, abstractmethod

class Membership(ABC):
    def __init__(self, email, card_number, gift_days=0, max_devices=0, cost=0):
        self._email = email
        self._card_number = card_number
        self._gift_days = gift_days
        self._max_devices = max_devices
        self._cost = cost

    @property
    def email(self):
        return self._email

    @property
    def card_number(self):
        return self._card_number

    @property
    def max_devices(self):
        return self._max_devices

    @property
    def cost(self):
        return self._cost

    def cancel_subscription(self):
        return FreeMembership(self._email, self._card_number)

class FreeMembership(Membership):
    def __init__(self, email, card_number):
        super().__init__(email, card_number, max_devices=1, cost=0)

    def change_subscription(self, new_type):
        if new_type in [1, 2, 3, 4]:
            return _create_new_membership(new_type, self._email, self._card_number)
        return self

class BasicMembership(Membership):
    def __init__(self, email, card_number):
        super().__init__(email, card_number, max_devices=2, cost=3000)

    def change_subscription(self, new_type):
        if new_type in [2, 3, 4]:
            return _create_new_membership(new_type, self._email, self._card_number)
        return self

class FamilyMembership(Membership):
    def __init__(self, email, card_number):
        super().__init__(email, card_number, gift_days=7, max_devices=5, cost=5000)

    def change_subscription(self, new_type):
        if new_type in [1, 3, 4]:
            return _create_new_membership(new_type, self._email, self._card_number)
        return self

class OfflineMembership(Membership):
    def __init__(self, email, card_number):
        super().__init__(email, card_number, gift_days=7, max_devices=2, cost=3500)

    def change_subscription(self, new_type):
        if new_type in [1, 2, 4]:
            return _create_new_membership(new_type, self._email, self._card_number)
        return self

class ProMembership(Membership):
    def __init__(self, email, card_number):
        super().__init__(email, card_number, gift_days=15, max_devices=6, cost=7000)

    def change_subscription(self, new_type):
        if new_type in [1, 2, 3]:
            return _create_new_membership(new_type, self._email, self._card_number)
        return self

def _create_new_membership(membership_type, email, card_number):
    if membership_type == 1:
        return BasicMembership(email, card_number)
    elif membership_type == 2:
        return FamilyMembership(email, card_number)
    elif membership_type == 3:
        return OfflineMembership(email, card_number)
    elif membership_type == 4:
        return ProMembership(email, card_number)
    else:
        return None

def main():
    print("Bienvenido al sistema de membresías.")
    
    # Solicitar email y número de tarjeta
    email = input("Ingrese su correo electrónico: ")
    card_number = input("Ingrese su número de tarjeta: ")
    
    # Mostrar opciones de membresía
    print("\nSeleccione el tipo de membresía inicial:")
    print("1. Gratis")
    print("2. Básica")
    print("3. Familiar")
    print("4. Sin Conexión")
    print("5. Pro")
    
    membership_type = int(input("Ingrese el número correspondiente al tipo de membresía: "))
    
    # Crear la membresía inicial
    if membership_type == 1:
        membership = FreeMembership(email, card_number)
    elif membership_type == 2:
        membership = BasicMembership(email, card_number)
    elif membership_type == 3:
        membership = FamilyMembership(email, card_number)
    elif membership_type == 4:
        membership = OfflineMembership(email, card_number)
    elif membership_type == 5:
        membership = ProMembership(email, card_number)
    else:
        print("Opción no válida.")
        return
    
    print(f"\nMembresía creada con éxito: {membership.__class__.__name__}")
    print(f"Costo: {membership.cost}")
    print(f"Dispositivos máximos: {membership.max_devices}")
    
    # Opción para cambiar la membresía
    print("\n¿Desea cambiar su membresía?")
    print("1. Básica")
    print("2. Familiar")
    print("3. Sin Conexión")
    print("4. Pro")
    
    new_type = int(input("Ingrese el número de la nueva membresía deseada (o cualquier otro número para mantener la actual): "))
    
    # Cambiar la membresía
    new_membership = membership.change_subscription(new_type)
    
    # Mostrar la nueva membresía
    print(f"\nSu nueva membresía es: {new_membership.__class__.__name__}")
    print(f"Costo: {new_membership.cost}")
    print(f"Dispositivos máximos: {new_membership.max_devices}")

if __name__ == "__main__":
    main()
