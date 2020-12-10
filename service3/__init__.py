import azure.functions as func
import random
import string

def main(req: func.HttpRequest) -> func.HttpRequest:
    for i in range(4):
        letter = ''.join(random.choice(string.ascii_lowercase))
        return letter
