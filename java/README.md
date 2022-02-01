# Examples for Java Presentation: "Smarter Types with Records"

A type defines a set of values. Historically we haven't been very good at
programming our classes to ensure that objects stay within that set of values.
This presentation looks at the problems with traditional OO encapsulation, and
presents a functional approach to Python type design, using frozen data classes
together with the data class `__post_init__()` function to guarantee the
constructed object is a legal value. Your code improves dramatically because now
you validate the object in one place, at construction. Freezing the object
guarantees it cannot be morphed into an illegal value. A typed object never
needs to be re-checked by any function that receives it as an argument.
