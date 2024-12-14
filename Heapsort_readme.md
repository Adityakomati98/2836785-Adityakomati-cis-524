# Heapsort Implementation

This repository contains two implementations of the Heapsort algorithm:
1. `Heapsort.py` - A Python implementation.
2. `Heapsort.c` - A C implementation.

## Prerequisites

### Python Version
- Python 3.x is required to run `Heapsort.py`.

### C Compiler
- A C compiler such as `gcc` is required to compile and run `Heapsort.c`.

## Files

1. `Heapsort.py`
   - Contains a Python implementation of Heapsort.
   - Demonstrates sorting a sample array and prints the results.

2. `Heapsort.c`
   - Contains a C implementation of Heapsort.
   - Demonstrates sorting a sample array and prints the results.

## Instructions to Run

### Running the Python Script

1. Ensure Python 3.x is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `Heapsort.py`.
4. Run the following command:

```bash
python3 Heapsort.py
```

5. The script will display the original array and the sorted array in the terminal.

### Running the C Program

1. Ensure a C compiler such as `gcc` is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `Heapsort.c`.
4. Compile the program using the following command:

```bash
gcc Heapsort.c -o heapsort
```

5. Run the compiled program:

```bash
./heapsort
```

6. The program will display the original array and the sorted array in the terminal.

## Sample Output

### Python
```
Original array: [12, 11, 13, 5, 6, 7]
Sorted array: [5, 6, 7, 11, 12, 13]
```

### C
```
Original array: 12 11 13 5 6 7 
Sorted array: 5 6 7 11 12 13 
```

## Notes

- Both implementations are hardcoded with a sample array for demonstration purposes.
- You can modify the input array in the respective files to test with different inputs.
- The Heapsort algorithm sorts the array in-place, ensuring efficient use of memory.

## Troubleshooting

### Python
- Ensure you have the correct version of Python installed.
- If you encounter a `ModuleNotFoundError`, verify the file name and ensure it is in the correct directory.

### C
- Ensure you have `gcc` or an equivalent compiler installed.
- If you encounter compilation errors, verify that the file is named correctly and is in the correct directory.

## License
This project is open source and free to use.
