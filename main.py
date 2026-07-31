users = {
        "banele": {"score": 50},
        "siya": {"score": 67},
        "busi": {"score": 73},
}
for name, data in users.items():
    if data["score"] > 20:
        users.pop(name)

print(users)

