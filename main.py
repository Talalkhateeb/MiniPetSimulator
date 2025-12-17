from pet import pet
p = pet("krkar",100)
print("pet name"+p.name)
print("pet energy level "+str(p.energy_level))
print("pet energy level after feed it "+str(p.feed_pet()))
print("pet energy level"+p.energy_level)
p.play_with_pet()
