from database import Database
from pprint import pprint
fields = ("name", "age", "height")
base = Database("People", *fields)

# for i in range(3):
#     base.insert(f"Nombre {i}", f"{30+i}", f"1.8{i}")

# base.delete(2)

#base.update(3, "Paul", 57, 1.73)

rS = base.select()
pprint(rS)
