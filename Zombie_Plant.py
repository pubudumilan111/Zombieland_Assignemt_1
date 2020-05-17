#Exercise 1
class Plant:
    def __init__(self, name, img, characteristic, cost, power, isRecharged):
        self.name = name
        self.img = img
        self.characteristic = characteristic
        self.cost = cost
        self.power = power
        self.isRecharged = isRecharged


class Zombie:
    def __init__(self, name, img, characteristic, health, toughness, accuracy, isRepeat):
        self.name = name
        self.img = img
        self.characteristic = characteristic
        self.health = health
        self.toughness = toughness
        self.accuracy = accuracy
        self.isRepeat = isRepeat

    def sun_cost(self):
        return (pow((self.health + self.accuracy), 5) - pow((self.health - self.accuracy), 2))*(self.accuracy / self.health)

pea_shooter = Plant('Pea-shooter', '', ['Defense', 'Shoot', 'Attack'], 100, 20, True)
sunflower = Plant('Sunflower', '', ['produce extra sun'], 50, 0, True)
wall_nut = Plant('Wall-nut', '', ['Defense'], 500, 300, True)

normal_zombie = Zombie('Normal-Zombie', '', ['Walk'], 100, 'low', 50.23, False)
cone_head_zombie = Zombie('Cone_Head_Zombie', '', ['Walk','Protect-head'], 250, 'medium', 60.34, False)
bucket_head_zombie = Zombie('Bucket_Head_Zombie', '', ['Walk', 'Run', 'Protect-head'], 500, 'high', 74.98, False)

#Exercise 2
print('Normal-Zombie_Cost', '=', (normal_zombie.sun_cost()))
print('Cone-Head_Zombie_Cost', '=', (cone_head_zombie.sun_cost()))
print('Bucket-Head_Zombie_Cost', '=', (bucket_head_zombie.sun_cost()))

#Exercise 3
secret_code = "plant_vs_zombies_2020i354D@#7"

print(secret_code[5:8])                                         # Slice between 6th and 8th character
print('20' in secret_code )                                     # Membership
print(secret_code.split('_'))                                   # Split
print(secret_code.upper())                                      # Capitalize
print("".join(list(map(lambda x: x, secret_code.split('_')))))  # Join
print(secret_code.replace('_', ' '))                            # Title
print(secret_code.replace('_', ' ').title())                    # Find
print(secret_code.find('20'))                                   # find '20'
print(secret_code.count('20'))                                  # count the number '20' inthe secrect code
