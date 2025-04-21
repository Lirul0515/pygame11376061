import os
current_path = os.path.dirname(__file__)
print(current_path)
parent_path = os.path.dirname(current_path)
print(parent_path)
image_path = os.path.join(parent_path,'res')
print(image_path)