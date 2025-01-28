from pathlib import Path

ruta = Path("./textos/")

string_objetivo = "Hola mundo"

for o in ruta.rglob("*.txt"):
    if o.is_file():
        text = o.read_text()
        if string_objetivo in text:
            print(o)

