import shelve

with shelve.open("mydata.db") as db:
    db["name"] = "Никита"
    db["age"] = 19
    db["city"] = "Лида"

with shelve.open("mydata.db") as db:
    print(db["name"])
