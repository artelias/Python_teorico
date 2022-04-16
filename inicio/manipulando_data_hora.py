"""
Manipulando data e hora
Python tem um modulo buil-in (ntegrado) para se trabalhar com data e hora
chamado datettime

#print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now())

#datatime.dateime(year, moth day, hour, minute,second, microsecond)
print(repr(datetime.datetime.now()))

#replace( paraa faaszer ajustes na data e hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horario para 16 horas, 0 inutos,0segundos 0microsegundos
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)
"""
import datetime
