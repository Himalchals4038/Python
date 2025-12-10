dict = {
    "One" : "First",
    "Two" : "Second",
    "Three" : "Third",
    "Four" : "Fourth",
    "Five" : "Fifth",
    "Six" : "Sixth",
    "Marks" : [15, 26, 34, 18, 29, 37],
    "dict1" : {
        "Ten" : 10,
        "Eleven" : 11,
        "Twelve" : 12,
        "Thirteen" : 13
    }
}
print(list(dict.items()))
print(list(dict.keys()))
print(list(dict.values()))

updateDict = {
    "Zero" : "None",
    "Poly" : "Multiple",
    "Mono" : "Single",
    "Six" : "Seventh"
}
dict.update(updateDict)
print(list(dict.keys()))
print(list(dict.values()))
print(dict.get("Mono")) #Returns None if key not found
print(dict["Mono"]) #Returns error if key not found

