from rich.console import Console
from rich.text import Text
from random import randint


def print_rainbow(text) -> None:
  console = Console()
  rainbow_text = Text()
  j = randint(1, 6)
  colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
  for i, char in enumerate(text):
      rainbow_text.append(char, style=colors[(j+i) % len(colors)])
  console.print(rainbow_text)


def mgl869() -> str:
  return print_rainbow(f"Démo MGL869")


def feature_1() -> str:
  return print_rainbow("Feature 1")

def feature_2() -> str:
  return print_rainbow("Feature 2")

if __name__ == "__main__":
  print_rainbow(mgl869())
