import os
class people:
    def __init__(self, name):
        self.name = name

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR, 'Uporabniki')

for root, dirs, files in os.walk(image_dir):
        for i in dirs:
            people(i)