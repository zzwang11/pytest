import visa

rm = visa.ResourceManager()
inst = rm.open_resource('zzz')
print(rm)
print(rm.list_resources())
# inst.