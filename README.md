# Incubyte-Chandrayaan_3-Assessment

## Introduction

This repository is the final outcome of the Coding Assessment by Incubyte inc.

## Getting Started

> Note: If you are using windows, use only python instead of python3 in following commands

### Cloning

Firstly clone this repository:

```
git clone https://github.com/HyperTextMachineLearning/Incubyte-Chandrayaan_3-Assessment.git
```

### Using

In `main.py` as you desire:
    - At line 23 edit `commands`
    - At line 24 edit `initial_coordinates` &
    - `2ND` argument to `MainProgram()` at line 25 (Note: Use any value in All-Caps except UP or DOWN)

Then at terminal run:

```
python3 src/main.py
```

## Tests

All modules are incrementally built and built upon by unit tests.

- To test all spacecraft functionalities (translation, rotation) run:

    ```
    python3 -m unittest src/translator/test_Translator.py
    ```

- To test the correctness of final position after all commands run:

    ```
    python3 -m unittest src/test_main.py
    ```

## Contact / Feedback

For any professional queries: work.ritik.matere@gmail.com
For any dev queries: dev.ritik.matere@gmail.com