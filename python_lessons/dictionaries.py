censav = { 'name': "MOU" , "age":20,"height":175 ,"weight":75}
censav[ "name"] = "Mustafa"
print(censav["age"])
print(censav["name"])

print(censav.get("name"))
print(censav.get("height",174))
print(censav.popitem())
print(list(censav.keys()))
print(len(censav))
print(censav)