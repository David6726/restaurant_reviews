from dataclasses import dataclass
from typing import Optional

@dataclass
class Error:
    code: str = None
    message: str = None
    
    def __init__(self, code, message):
        self.code = code
        self.message = message

@dataclass
class Result:
    data:any = None
    error: Optional[Error] = None

    def __init__(self, data = None, error = None):
        self.data = data
        self.error = error


def make_data_result(data):
    return Result(data=data)

def make_error_result(code, message):
    return Result(error=Error(code, message))
