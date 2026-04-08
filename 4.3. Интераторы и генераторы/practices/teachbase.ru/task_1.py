from typing import Self


class RangeIterator:
    def __init__(self, start: int, end: int) -> None:
        self.start: int = start
        self.end: int = end
        self.current: int = start
    
    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> int:
        if self.current >= self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value
        
    
    
inter_range = RangeIterator(1, 10)
for i in inter_range:
    print(i)