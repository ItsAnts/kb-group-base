from time import time, sleep
from typing import Any, Optional

def min_time(seconds: int) -> Any:
    def wrap(func) -> Optional[Any]:
        def called(*args, **kwargs) -> Optional[Any]:
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            if end_time - start_time < seconds:
                sleep(seconds - (end_time - start_time))
            return result
        return called
    return wrap

@min_time(seconds=1)
def task():
    print("Run")
    
task()