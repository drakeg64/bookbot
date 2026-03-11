# BookBot

BookBot is a Python application that analyzes books and generates statistical reports about them. It processes text files and provides insights such as word frequency, character counts, and other text analytics.

## Features

- **Word Count Analysis**: Generates detailed word frequency statistics
- **Character Statistics**: Analyzes character distribution and usage patterns
- **Easy to Use**: Simple command-line interface for quick analysis
- **Extensible**: Modular design makes it easy to add new analysis features

## Installation

1. Clone the repository:
```bash
git clone https://github.com/drakeg64/bookbot.git
cd bookbot
```

2. No external dependencies required - uses only Python standard library!

## Usage

1. Place your book files (.txt format) in the `books/` directory
2. Run the main script:
```bash
python main.py
```

The script will process the books and output statistical analysis to the console.

## Project Structure

- `main.py` - Main entry point for the application
- `stats.py` - Contains statistics generation functions
- `books/` - Directory for storing book files to analyze

## About

BookBot is my first [Boot.dev](https://www.boot.dev) project!