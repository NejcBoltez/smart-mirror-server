import os
class people:
    def __init__(self, name):
        self.name = name
        print(name)

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')
Users_table=[]
for root, dirs, files in os.walk(image_dir):
        for i in dirs:
            Users_table.append(people(i))
print(Users_table[0].name)