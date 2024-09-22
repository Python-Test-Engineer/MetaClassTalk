import math
import random
from rich.console import Console

console = Console()


class Pizzabase(metaclass=type):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return round(math.pi * self.radius**2, 2)


type(Pizzabase), Pizzabase.__name__


p = Pizzabase(10)
p.area()


CUSTOM_COUNTER = 0


class MyCustomType(type):
    # Pizzabase, (,)
    def __prepare__(class_name, inherited_classes):
        console.print("[cyan bold italic]__prepare_ called...[/]")
        console.print(
            f"[cyan]Using custom metaclass __prepare__ with class_class_name {class_name} and Inherited Classes {inherited_classes}[/]\n"
        )

        return {}

    def __new__(metacls, class_name, inherited_classes, class_body):

        console.print("[gold1 bold italic]__new__ called...[/]")

        print(f"Using custom metaclass {metacls} to create class {class_name}...\n")
        print(
            f"[gold1]Developer can now run organisation validations here by adding metaclass {metacls} to class {class_name}...[/]\n"
        )

        if not class_name.istitle():

            raise ValueError("Class class_name must start with an uppercase letter")

        else:

            console.print("[gold1]GOOD JOB! Title case used.[/]")

        # print(vars(class_name)) class_name is just a string not the class object
        cls_obj = super().__new__(metacls, class_name, inherited_classes, class_body)

        cls_obj.circ = lambda self: round(2 * math.pi * self.radius, 2)

        return cls_obj

    def __call__(cls, *args, **kwargs):
        console.print("==========================================================")
        console.print("[bright_yellow bold italic]__call__ called...[/]")

        console.print(f"[bright_yellow]Calling {cls} with {args} and {kwargs}[/]")
        if cls.__dict__["__doc__"] is not None:
            console.print(f"[bright_yellow]Good job! You added a doc string:[/]")
            console.print(f"\n\t[bright_yellow]{cls.__dict__['__doc__']}[/]\n")
        else:
            raise ValueError("You forgot to add a doc string.")

        console.print("[bright_yellow]We can record how often the class is called.[/]")
        # some DB etc...
        global CUSTOM_COUNTER
        CUSTOM_COUNTER += 1
        console.print(
            f"[bright_yellow]{cls} has been called {CUSTOM_COUNTER} times[/]\n"
        )
        console.print("==========================================================")

        return super().__call__(*args, **kwargs)


class Pizzabase(metaclass=MyCustomType):
    """Pizaabase class using MyCustomType metaclass"""

    def __init__(self, radius):
        console.print(
            f'[green_yellow bold italic]\n__init__ being called with radius {radius}"[/]'
        )

        self.radius = radius

    def area(self):

        return round(math.pi * self.radius**2, 2)


# NB the __call__ method is not called


vars(Pizzabase)


p = Pizzabase(random.randint(1, 10))
console.print(f"\n[orange1]Pizza Circumference {p.circ()}[/]")
console.print(f"[orange1]Pizza areas {p.area()}[/]\n")
