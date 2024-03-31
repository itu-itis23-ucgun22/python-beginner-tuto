dogs = ["Roger",1,True,"karabas"]

dogs[3]="bozkurt"



dogs.append("Toni")
dogs.extend(["çakal",5])
dogs += ["prenses"]
dogs += "syd"
dogs.remove(1)
dogs.pop(5)
dogs.insert(0,"yavru")
dogs[2:2] = ["kılıbık","korkak"]
dogs.remove(1)
dogs.sort(key = str.lower) # sorted(dogs,key = str.lower)

print(dogs)