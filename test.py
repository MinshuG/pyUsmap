from Usmap import Usmap

with open("++Fortnite+Release-15.10-CL-15014719-Windows_oo.usmap", "rb") as f:
    data = Usmap(f).read()
    print("Done")