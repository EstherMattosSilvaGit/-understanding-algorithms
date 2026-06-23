# Understanding Algorithms

This repository contains implementations and exercises from the **"Grokking Algorithms"** book by Aditya Bhargava.

## About This Repository

This project is designed to help beginners understand and implement fundamental algorithms. Each algorithm is organized in its own folder with:
- **Algorithm implementation** - The core algorithm code
- **Tests** - Unit tests to verify correctness
- **Example file** - Easy-to-understand examples with hardcoded values

## Project Structure

```
BinarySearch/
├── binarySearch.py          # Algorithm implementation
├── BinarySearchTests.py      # Unit tests
├── example.py               # Beginner-friendly examples
└── BinarySearch.md          # Algorithm explanation
```

## How to Run

### Run All Tests
```bash
make test
```

This command discovers and runs all `*Tests.py` files in the repository using Python's `unittest` framework.

### Run Algorithm Examples
Each algorithm folder has an `example.py` file with hardcoded values to help you understand how the algorithm works:

```bash
python -m BinarySearch.example
```

The example file includes:
- ✅ Pre-defined test cases
- ✅ Clear output showing results
- ✅ A section where you can modify values to experiment

### Clean Cache
```bash
make clean
```

Removes Python cache files (`__pycache__`, `.pytest_cache`) from the project.

## Available Commands

| Command | Description |
|---------|-------------|
| `make test` | Run all tests |
| `make clean` | Remove Python cache files |
| `make help` | Show available commands |

## Adding New Algorithms

1. Create a new folder (e.g., `QuickSort/`)
2. Add your algorithm implementation
3. Create a `*Tests.py` file with unit tests
4. Optionally, create an `example.py` file for beginners
5. Run `make test` to verify everything works

## Learning Approach

- 📖 Study the algorithm concept
- 💻 Read the implementation
- 🧪 Run the unit tests to understand edge cases
- 🎓 Run the example file to see practical usage
- 🔧 Modify the example values and experiment

## Technologies

- Python 3.x
- unittest (for testing)
- Make (for task automation)
