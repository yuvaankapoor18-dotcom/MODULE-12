Gradebook = {"Alice": 50,
            "John": 46,
            "Jack": 39,
            "Glenda": 30,
            "Howard": 29}

def average(x):
    return x/5
def maximum(x):
    return max(x)
print("average =",average(185))
print("maximum =",maximum([50, 46, 39, 30, 29]))

def minimum(x):
    return min(x)
print("minimum =",minimum([50, 46, 39, 30, 29]))
name = (input("Whose score do you wanna check?(Alice/John/Jack/Glenda/Howard):  "))
if name == "Alice" or name == "alice":
  print(Gradebook.get("Alice"))

elif name == "John" or name == "john":
  print(Gradebook.get("John"))

elif name == "Jack" or name == "jack":
   print(Gradebook.get("Jack"))

elif name == "Glenda" or name == "glenda":
   print(Gradebook.get("Glenda"))

elif name == "Howard" or name == "howard":
   print(Gradebook.get("Howard"))

else:
   print("Name not found.")