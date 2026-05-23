from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
    active: bool = True

    def greet(self) -> str:
        """Return a personalized greeting."""
        return f"Hi, my name is {person.name} and I'm {person.age} years old."

if __name__ == "__main__":
    person = Person(name="Edgar", age=25, email="edgarmlmp@gmail.com")
    print(person.greet())
