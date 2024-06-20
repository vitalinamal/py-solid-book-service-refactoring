from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReversePrint
from app.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book)
            elif method_type == "reverse":
                ReverseDisplay().display(book)
        elif cmd == "print":
            if method_type == "console":
                ConsolePrint().print(book)
            elif method_type == "reverse":
                ReversePrint().print(book)
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerialize().serialize(book)
            elif method_type == "xml":
                return XmlSerialize().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
