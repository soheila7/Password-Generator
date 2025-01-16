This repository contains a Python-based password generator with different strategies to create passwords:

- **PIN Code Generator**: Generates a numeric PIN code of a specified length.
- **Random Password Generator**: Generates a random password with optional inclusion of numbers and special symbols.
- **Memorable Password Generator**: Generates a password made of random words from the NLTK corpus, with optional capitalization and custom separators.

## Features

- **PIN Code Generator**: Generates a numeric PIN code with a default length of 4.
- **Random Password Generator**: Generates a random password consisting of alphabets, and optionally numbers and symbols. The default length is 8.
- **Memorable Password Generator**: Creates a memorable password by combining random words with an optional separator. The default password contains 5 words, with optional capitalization.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/soheila7/Password-Generator.git
    cd password-generator
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    **Note:** You may need to install `nltk` if it's not already installed. You can install it using:
    ```bash
    pip install nltk
    ```

3. Download the required NLTK data:
    ```bash
    python -m nltk.downloader words
    ```

## Usage

To run the password generator, execute the Python script:

```bash
python src/password_generator.py
```
This will generate and print:

- A random **PIN code** (default length: 4).
- A random **password** (default length: 8).
- A **memorable password** (default: 5 words separated by `-`).

You can also modify the defaults by passing arguments to the classes in the script. For example:

- **PIN Code Generator**: Change the length by passing the `length` parameter.
- **Random Password Generator**: Set the password length and inclusion of numbers and symbols by passing the `length`, `include_num`, and `include_symb` parameters.
- **Memorable Password Generator**: Customize the number of words, separator, and capitalization by passing the `num_words`, `separator`, and `capitalization` parameters.

## Example Output

```plaintext
5650
soauvWBL
multitube-autopsychic-arbalist-stormlessness-twae
```
- The first line is the generated PIN code.
- The second line is the random password generated.
- The third line is a memorable password consisting of words from the NLTK corpus.

## Code Overview

The code contains the following classes:

- **Passwordgenerator(ABC)**  
  An abstract base class for all password generators with an abstract method `generator()`.

- **Pincodegenerator**  
  Generates a numeric PIN code of a specified length.

- **Memorable**  
  Generates a memorable password consisting of a sequence of words from the NLTK corpus, optionally capitalized and joined with a separator.

- **Randompassword**  
  Generates a random password of a specified length, with optional inclusion of numbers and special symbols.

- ### **Functions**

    - **pin_code()**: Generates and prints a PIN code.
    - **random_password()**: Generates and prints a random password.
    - **memorable_generator()**: Generates and prints a memorable password.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
