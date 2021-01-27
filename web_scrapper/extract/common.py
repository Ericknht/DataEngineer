import yaml

# Esta variable nos va a servir para cachear nuestra configuración
# Es importante hacer esto, porque estamos leyendo a disco, y si queremos utilizar
# nuestra configuración en varias partes de nuestro código,
# no queremos leer a disco cada vez que queramos utilizar la configuración.
__config = None

def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f, Loader=yaml.FullLoader)
    return __config