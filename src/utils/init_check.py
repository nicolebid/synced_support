import os 
from ..config import STUDENT_DATA

def is_initialized():
    print(os.path.exists(STUDENT_DATA))
    return os.path.exists(STUDENT_DATA)

if __name__ == "__main__":
    is_initialized()