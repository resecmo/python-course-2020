import asyncio


def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"


def establish_connection(auth=True):
    import random
    user_id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {user_id}"
    yield from user_connection(user_id)
    if auth:
        yield f"disconnect {user_id}"


def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


async def write_to_file(file):  # TODO
    file.write("test")


async def connect_user():  # TODO
    f = open("aa.txt", "w")
    await write_to_file(f)
    f.close()


def scheduler():  # TODO
    for i in connection():
        print(i)


scheduler()
