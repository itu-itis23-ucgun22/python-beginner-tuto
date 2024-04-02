try:
    raise Exception('an error')
except Exception as error:
    print(error)


class DogNotFound(Exception):
    pass

try:
    raise DogNotFound
except DogNotFound:
    print("dog not found")