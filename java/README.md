# Examples for Java Presentation: "Smarter Types with Records"

A type defines a set of values. Historically we haven't been very good at using
encapsulation to ensure that objects stay within that set of values. This
code-focused presentation provides a functional approach to Java type design,
using Java's new `record` keyword to guarantee that each constructed object is a
legal value. Your code improves dramatically because now you validate the object
in one place, at construction. Because `record` fields are automatically
`private`, an object cannot be morphed into an illegal value. A typed object
never needs to be re-checked by any function that receives it as an argument.
