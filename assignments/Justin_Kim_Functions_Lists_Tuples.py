zoo_animals = []

for i in range(5):
    animal = input(f"Enter species of animal {i+1}: ").lower()  
    zoo_animals.append(animal)

print("Zoo Animals:", zoo_animals)

lion_count = zoo_animals.count("lion")
panda_count = zoo_animals.count("panda")
bear_count = zoo_animals.count("bear")

print(f"Lions: {lion_count}, Pandas: {panda_count}, Bears: {bear_count}")
