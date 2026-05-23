**Afan Oromo Beginner Language (AOBL) – Condensed Specification** 

## **Introduction** 

The Afan Oromo Beginner Language (AOBL) is a beginner-oriented programming language designed to make programming easier and more accessible for Afan Oromo speakers. The language translates Afan Oromo source code into executable Python 3 code while maintaining a structured compiler architecture. AOBL aims to reduce the English syntax barrier commonly faced by beginners learning programming concepts for the first time. By using familiar Afan Oromo terminology, the language provides a more comfortable and intuitive learning environment while still introducing standard programming principles. 

## **Design Objectives** 

The primary goal of AOBL is to provide a simple and educational programming language that emphasizes readability and ease of understanding. The language uses familiar Afan Oromo vocabulary to represent programming constructs, allowing learners to focus on computational thinking instead of struggling with foreign terminology. In addition, AOBL supports safe type checking and maintains a direct relationship with Python concepts, enabling learners to smoothly transition to standard Python programming after gaining foundational skills. 

## **Language Structure and Keywords** 

AOBL includes a small but effective set of keywords that cover essential programming concepts such as variables, conditions, loops, functions, logical operations, and exception handling. The keyword “haa” is used for variable declaration, while “yoo,” “yoo_tahe,” and “yookaan” are used for conditional statements. Looping structures are implemented using “hanga” and “irra … keessa.” Functions are defined with “hojii,” and return statements use “deebi'i.” Output operations are performed using “maxxansi.” Logical operations are represented by “fi,” “yookiin,” and “miti,” while exception handling uses “yaali,” “qabsiisi,” and “dhuma.” 

## **Type System and Syntax** 

AOBL supports a basic type system with localized type names. The type “lakkoofsa” represents integers, “lakkf” represents floating-point numbers, “barruu” represents strings, and “dhugaa” represents Boolean values. Variable declarations and expressions closely resemble Python syntax while remaining easy to understand for beginners. 

For example, a variable may be declared as: haa x: lakkoofsa = 5 Conditional statements are written in a natural form such as: yoo x > 5: maxxansi("Greater") Loops and functions follow a similarly readable structure: hanga x < 4: x = x + 1 

hojii ida(a, b): deebi'i a + b 

The language also follows a clear operator precedence order, beginning with parentheses and unary operations, followed by multiplication and division, addition and subtraction, comparison operations, logical AND operations, and finally logical OR operations. 

## **Compiler Pipeline and Error Handling** 

AOBL follows a structured compilation process that transforms source code into valid Python code. The process begins with lexical analysis, where the source text is converted into tokens. The parser then constructs an Abstract Syntax Tree (AST) to validate the syntax structure. After parsing, the type checker verifies type consistency throughout the program. Finally, the code generator produces executable Python 3 code. 

The language also emphasizes accessibility through localized error messages written entirely in Afan Oromo. Errors such as indentation mistakes, type mismatches, missing tokens, and invalid syntax are clearly reported in a way that beginner learners can easily understand. 

## **Current Limitations** 

The current version of AOBL is intentionally minimal and does not yet support advanced programming features such as classes, modules, dictionaries, sets, decorators, asynchronous programming, or advanced type hints. These limitations were introduced to keep the language simple and beginner-friendly during the first stage of development. Future versions of the language may gradually introduce more advanced features as the project evolves. 

## **Conclusion** 

The Afan Oromo Beginner Language demonstrates how programming languages can be adapted to local languages and cultures in order to improve accessibility and learning outcomes. By combining familiar Afan Oromo terminology with structured compiler design and direct Python compatibility, AOBL provides a strong educational foundation for beginner programmers while promoting inclusive access to programming education. 

