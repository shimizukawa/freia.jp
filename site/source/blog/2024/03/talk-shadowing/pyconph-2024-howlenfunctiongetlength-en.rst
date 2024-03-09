:orphan:

pyconph-2024-howlenfunctiongetlength-en
==========================================

.. code-block:: markdown

    Hello everyone,
    First off, let me introduce myself.

    ##
    My name is Takayuki Shimizukawa.

    I have been living in BGC, Manila for 7 months now.
    I love spicy food and my favorite Filipino dish is sisig.
    I also love craft beer.

    I have been using Python since 2004.
    My main activities are as follows:
    * I am the accounting director of the "PyCon JP Association."
    * I work fully remotely for a Japanese company called BeProud.
    * I have translated and written 13 Python-related books in 13 years.

    So, let's get started!

    ##
    How does Python get the length of something using the `len()` function?

    ##
    This presentation is aimed at those who:
    * Have started learning Python but feel something's not quite clicking.
    * Wonder why `len` is a function, not a method.
    * Think Python isn't object-oriented.
    If you have these questions, you're in the right place.
    This material is designed for those looking to move from beginner to intermediate level in Python.

    ## 
    Here's the agenda for the talk.
    There are three parts, and the first one, "How does len() get the length of an object?" is the most important part of this slide.
    The second part introduces a slightly different example based on the first.
    The third part is a bit more complex, but I will skip it today due to limited time. I hope you will refer to the slides later.
    Finally, there will be a summary and references.

    Let's move on to part one.

    ##
    Part1
    How does `len()` get the length of an object?
    This part is beginner level.
    Think of the chili as indicating difficulty.

    ##
    What happens inside of `len()` function?

    For example, let's pass a string "Kuya".
    It returns 4.

    Next, call underscore, underscore, len, underscore, underscore, parentheses, ... 
    Too long, isn't it?
    This is called the dunder len method.

    So when you call dunder len, 4 is returned.
    This is the same as the first result.
    Actually, `len(obj)` internally calls `obj.__len__()` method.

    ##
    Wasn't `len()` necessary?

    If there's an `.__len__()` method, why not just use that?
    In Java or JavaScript, we can get the length using `.len` or `.length` properties.
    Why does Python use the `.__len__()` method?

    ##
    Actually, `len()` function does a bit more.

    In this green part, it checks if the value returned by the string object is an `int` type.
    If it's not an `int` type, it throws a `TypeError` exception.

    This is how the `len()` function guarantees an `int` is returned.

    By the way, did you see the top right of the slide?
    The chili is gradually getting longer!

    ##
    If `__len__()` returns a non-int value...

    I wrote this code to see what happens.
    If dunder len returns `1.2`, a `float` type, you get the error "float object cannot be interpreted as an integer".
    There are other exceptions if you exceed `sys.maxsize`.

    ##
    The responsibility of the `len()` function is to call the object's `.__len__()` method, check the obtained value, and return the appropriate value to the caller.

    This is called the Adapter pattern, which performs interface conversion.
    The `len()` function adapts the object, extracts the value, processes it, and returns the result.

    Visually, `.__len__()` is split into two, but the left side shows that the string object implements this method. The right side's green square showing `.__len__()` means, "This is the interface the `len()` function will use."

    ##
    So, what is the Adapter pattern?
    I think you might have heard of it before.

    I'll leave the details to Wikipedia, but hopefully, you get the idea from the picture.
    It's like a power adapter converting AC from 100 volts to 240 volts into 20 volts 3 amps of DC.
    An adapter changes the interface to get the appropriate value.
    Some power adapters also won't output if the input is invalid.

    ##
    The `len()` function acts as an Adapter for specific objects.
    Specific means, objects that adapts to the protocol of returning a numerical value through the `.__len__()` interface.
    If the `len()` function receives a non-numeric type, it will raise a `TypeError` exception.

    ##
    Apply the `len()` Adapter to list.
    Specifically, a `list` adapts to the len Adapter.

    The `list.__len__()` method returns the number of elements.
    The list object knows its number of elements, which is 3, so `.__len__()` method returns 3.
    The `len()` Adapter checks this value and finally returns 3.

    ##
    Apply the `len()` Adapter to dict.

    `dict` also has a `.__len__()` method that returns the number of keys.
    For example, if a `dict` has age: 999, name: Kuya, it has two keys, so it returns 2.

    ##
    Now, let's try the len Adapter with a custom data type.
    As mentioned, if there's a `.__len__()` method, it can work with the len Adapter, so implementing `.__len__()` method will make it work.
    This Random class returns a result from `random.randint(0,10)` in its `.__len__()` method.
    It's a strange class whose length changes with each call.
    Thus, a class that adapts to the len Adapter can be easily implemented.

    ##
    A protocol defines the behavior of objects.
    The `len()` function works if there's an `obj.__len__()` method.
    In other words, objects with length must implement the `. __len__()` method.
    Implementing this `.__len__()` method is called "implementing the length protocol."

    ##
    I've been talking about protocols, but where does Python's documentation describe them?
    I've been asked where to find protocols in the documentation.
    Looking for it, protocols appear in about 4-5 pages of the official Python documentation, especially around terms like sequences and iterators.

    ##
    Protocols first appeared in Python documentation in Python 2.2, when classes were introduced to Python.
    I also checked to see if there is a protocol definition in PEP.
    The first mention of protocols in PEPs was in May 2017's PEP-544.
    PEP-544 was created to define the term protocol for the introduction of type hints.

    ##
    The `collections.abc` document could be used in place of the protocol list.
    I was looking for a protocol list and found this.
    Here is the list of methods that should be supported for different types of collections.
    It says that Sized collections should have a `.__len__()` method.

    ##
    Summary so far.
    `len()` is an Adapter for an object.
    Protocols are conventions for communication between objects and Adapters.

    ##
    So far I have explained that "len is Adapter".
    However, some people may say, "Adapter is just a function that checks if it is `int` or not, right? Couldn't it have been a `.length` attribute?" You may think, "Why not implement it as a `.length` attribute?

    Here's a quote from "Design and History FAQ" docs:
    As Guido said: (b) When I read code that says len(x), I know it's asking for the length of something. This tells me two things: the result is an integer, and the argument is some kind of container.

    ##
    That concludes part one.
    So far, I've covered chili level1,
    but next, I'll introduce an example with if statements based on what I've discussed at Part1.

    ##
    Part2.
    How if statements determine an object's True or False.
    This is level 2 spicy.

    ##
    About if statement.

    Here's an example of an if statement: if some object is true, it shows "True", and if not, it shows "False."
    Internally, it's automatically passed to the bool function and converted.
    So, let's start calling the bool function an Adapter instead of a function.

    ##
    What happens inside of `bool()` adapter?

    The bool Adapter judges the truthfulness of objects.
    For example, if you pass the number 42, it returns True.
    You might guess it's calling `obj.__bool__()` inside, right? Well, that's correct.
    It's the same as len adapter we discussed earlier.
    So, next, let's try it with a string.

    ##
    What happens inside of `bool()` adapter with string argument?

    With string, oops, directly calling the string object's `.__bool__()` method cause an error:
    `Attribute Error 'str' object has no attribute '__bool__'`.

    So, let's check the specifications of the `bool()` function in the documentation.

    ##
    Rule to convert number and string by `bool()`

    The following is a quote from the official reference:

    * An object is considered false: If the class defines `__bool__()` or `__len__()` methods, they return the integer 0 or the False.
    * An object is considered true: if it's not considered False.
    This means there's a bit more checking involved than with the len adapter, so it seems like it's doing more work.

    ##
    Let's introduce the mechanism of the bool Adapter with a diagram.

    If there's no `.__bool__()` method, it does something equivalent to `bool(len(obj))`.
    First, let's look at the `.__bool__()` method.
    `bool()` adapter checks if there's a `.__bool__()` method and uses it to extract a boolean value. If a boolean type is returned, it uses that value; otherwise, it throws a `TypeError` exception.

    If there's no `.__bool__()` method, it internally performs a process equivalent to the len adapter and passes the result to a process equivalent to boolean.
    Since len always returns a number, it can use the `int.__bool__()` method.

    This is the job of the bool Adapter. I looked up the implementation code of the bool Adapter in CPython for verification, so if you're interested, please read it. This is level 6 spicy I think.

    ##
    Next, let's try using the bool Adapter with a custom data type.
    I'll implement the PositiveInt class.
    It's true for positive integers.
    What it does is; inherit `int` and implement a `.__bool__()` method that returns `True` if `self` is greater than zero.
    In practice, 10 returns `True`, and minus 3 returns `False` because it's not greater than zero.

    That concludes our discussion on truth determination in if statements.

    ##
    Part 3 would have been about how for loops obtain iteration from objects, but I'll skip it due to limited time.
    I hope you will refer to the slides later.

    ##
    Summary

    ##
    To wrap up,
    In today's talk, I've introduced Adapter and protocol through examples of len and bool.
    Doesn't it make sense to call len an Adapter pattern?
    I hope this talk makes you feel that Python is not non-object-oriented just because of the len function.
    If you like design patterns, seeing it as an adapter pattern might be satisfying.

    Regarding the `len` function versus `.length` attribute.
    Let's put your own preference aside for now.
    Even just looking at the `len()` function, you can see that there's been a lot of discussion about why the language specification is the way it is today.
    I followed the history while creating this slide and found a huge amount of information.
    I think it is a good way to learn a programming language by following such discussions and reading the implementation code.

    Also, there's a lot of information in the official reference.
    Most of the quotes today were from the official reference.
    I think reading the PEPs will be one of the challenges.

    How to progress from beginner to intermediate?
    Let's just read the numerous documents referenced in this slide.
    And it would be interesting to interpret them in your own way, implement them in Python, and discover things like, "Something doesn't work as expected," or "It's not consistent," or "This part doesn't have the name of the protocol.
    By doing this, I think knowledge will naturally accumulate.

    ##
    The following are references.
    (skip reading)

    ##
    Thank you for coming my talk and also thanks to the event staffs.
    This concludes my presentation.
    Does anyone have any questions or comments?
