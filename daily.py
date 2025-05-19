from config import printers, data_file, error_log
from hp_printers import page_count
import datetime

data = open(data_file, "a")
log = open(error_log, "a")

for printer in printers:
    ip = printer+".ime.usp.br"
    date = str(datetime.datetime.now().date())
    try:
        counter = str(page_count(ip))
        line = printer + "," + date + "," + counter + "\n"
        data.write(line)
    except:
        log.write("Impressora "+printer+" não encontrada.\n")

data.close()
log.close()
