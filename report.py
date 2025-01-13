from hp_printers import page_count

printers = [
    "escada",
    "compasso",
    "moby",
    "graficacolor",
    "graficamono1",
    "graficamono2",
    "graficamono3",
    "keynes",
    "alexandria",
    "folha",
    "rosa",
    "rec",
    "led",
    "farofa",
    "hp",
    "earl"
]

for printer in printers:
    ip = printer+".ime.usp.br"
    try:
        print("Total "+printer+" - "+page_count(ip))
    except:
        print("Impressora "+printer+" não encontrada.")
