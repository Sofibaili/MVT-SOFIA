from AppFamilia.models import Familiar

Familiar(nombre="Carlos", direccion="9 de julio 2322", numero_pasaporte=123123).save()
Familiar(nombre="Laura", direccion="9 de julio 2322", numero_pasaporte=890890).save()
Familiar(nombre="Luca", direccion="9 de julio 2322", numero_pasaporte=345345).save()
Familiar(nombre="Julian", direccion="9 de julio 2322", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")
