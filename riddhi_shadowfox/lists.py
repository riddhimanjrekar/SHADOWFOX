
# Initial Justice League Members

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1.
num_members = len(justice_league)
print("\n1. Number of Members in Justice League:", num_members)

# 2.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)

# 3.
justice_league.remove("Wonder Woman")     
justice_league.insert(0, "Wonder Woman")   
print("\n3. After making Wonder Woman the leader:", justice_league)

# 4.
justice_league.remove("Superman")  
flash_index = justice_league.index("Flash")  
justice_league.insert(flash_index, "Superman")  
print("\n4. After separating Aquaman and Flash:", justice_league)

# 5.
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League Members:", justice_league)

# 6.
justice_league.sort()
print("\n6. Justice League after sorting:", justice_league)
print("The new leader (index 0) is:", justice_league[0])

