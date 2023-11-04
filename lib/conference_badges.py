def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    messages = []
    for name in names:
        messages.append(f"Hello, my name is {name}.")
    return messages

def assign_rooms(names):
    room = []
    for i in range(len(names)):
        num = i + 1
        message = f"Hello, {names[i]}! You'll be assigned to room {num}!"
        room.append(message)
    return room

def printer(names):
    batchs = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for batch in batchs:
        print(batch)
    for room in rooms:
        print(room)

