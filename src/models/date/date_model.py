from dataclasses import dataclass


@dataclass
class DateModel():
    start_in_ms: int;
    end_in_ms: int;