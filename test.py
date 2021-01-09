from Usmap import Usmap

with open("++Fortnite+Release-15.10-CL-14937640-Windows_br.usmap", "rb") as f:
    data = Usmap(f).read()
    print("Done")