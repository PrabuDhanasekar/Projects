# Word Count

class TagCloud:
    def __init__(self):
        self.tags ={}

    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0)+1

num_inputs = int(input("How many inputs do you want to enter? "))

inputs = []
cloud = TagCloud()
for _ in range(num_inputs):
    value = input("Enter a value: ")
    inputs.append(value)
    cloud.add(value)

# print("Inputs are:", inputs)
print(cloud.tags)