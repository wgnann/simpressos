from config import printers
from hp_printers import page_count

for printer in printers:
    ip = printer+".ime.usp.br"
    try:
        print("Total "+printer+" - "+str(page_count(ip)))
    except:
        print("Impressora "+printer+" não encontrada.")
