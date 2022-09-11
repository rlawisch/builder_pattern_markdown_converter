# Builder Pattern example - Markdown converter

This project is a simple, naïve implementation of a subset of the Markdown specification to demonstrate the [Separation of Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle offered by the [Builder pattern](https://en.wikipedia.org/wiki/Builder_pattern). It converts H1-H6, bold and italics with asterisks and unordered lists with no sub-list detection, all with regex and in the most naïve way found.
It is made in Python 3 with 0 dependencies to install. Running is as simple as `python3 main.py`, and to run the tests is just `python3 tests.py`.
Currently, we only have an implementation to convert Markdown to HTML, but adding a new ouput format is as simple as implementing a new `TextConverter` concrete inheritance.

Pull requests with refactors, better/more complete implementations of the Markdown format specification, exception handling and/or better coverage of edge cases are very welcome!
