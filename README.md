# FastAPI Template

## Description

This is a FastAPI-based template, it should be use as a starting point for new projects. It includes a basic structure for the project, with a simple API and some development tools.

## Features

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.12+.
- **Starlette**: Lightweight ASGI framework for building async web applications.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **IPython and IPykernel**: Enhanced interactive Python shell and kernel.
- **HTTPX**: Fully featured HTTP client for making requests.
- **Development Tools**: Includes tools for code formatting, linting, and testing.

## Installation

To install Core, you need to have Python 3.12 or higher. You can then use Poetry to manage dependencies and environment setup. Follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:

   ```bash
   poetry install
   ```

## Usage

After installation, you can use the provided scripts to run various commands:

- **Start the application**:

  ```bash
  poetry run start
  ```

- **Lint the code**:

  ```bash
  poetry run lint
  ```

- **Run tests**:

  ```bash
  poetry run test
  ```

## Development

For development, make sure you have the necessary development dependencies installed. You can use the following command to install them:

```bash
poetry install --with dev
```

### Code Style and Quality

- **Black**: Code formatter
- **Flake8**: Linter
- **Bandit**: Security linter
- **Isort**: Import sorter

### Testing

- **pytest**: Testing framework
- **pytest-mock**: Mocking library
- **pytest-cov**: Coverage reporting
- **pytest-asyncio**: Support for testing async code
- **pytest-httpx-blockage**: Plugin for testing HTTPX requests

## Contributing

Contributions are welcome! Please follow the standard GitHub flow for contributing:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
