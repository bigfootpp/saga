import time
from typing import Self


class Stopwatch:
    def __init__(self, paused: bool = False) -> None:
        self.paused = paused
        self.accumulated_time = 0.0
        self.start_time = time.perf_counter()

    def pause(self):
        if self.paused:
            return
        self.accumulated_time += time.perf_counter() - self.start_time
        self.paused = True

    def resume(self):
        if not self.paused:
            return
        self.start_time = time.perf_counter()
        self.paused = False

    def reset(self, paused: bool = False):
        self.paused = paused
        self.accumulated_time = 0.0
        self.start_time = time.perf_counter()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pause()

    @property
    def time(self) -> float:
        if self.paused:
            return self.accumulated_time
        else:
            return self.accumulated_time + (time.perf_counter() - self.start_time)
