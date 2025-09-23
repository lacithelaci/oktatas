from dataclasses import dataclass


@dataclass
class Person:
    id: str
    name: str
    age: int
    male: bool

@dataclass
class Car:
    plate: str
    type: str
    year: int
    automatic: bool

@dataclass
class Airport:
    code: str
    name: str
    city: str
    state: str
    country: str


