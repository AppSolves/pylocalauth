<p align="center">
  <kbd><img src="https://raw.githubusercontent.com/AppSolves/pylocalauth/refs/heads/main/assets/github/repo_card.png?sanitize=true" alt="pylocalauth"></kbd>
</p>
<br>

# `pylocalauth`

<p align="center">Cross-platform local authentication library for Python applications.</p>
<br>

[![build](https://github.com/AppSolves/pylocalauth/workflows/Build/badge.svg)](https://github.com/AppSolves/pylocalauth/actions)
[![PyPI version](https://badge.fury.io/py/pylocalauth.svg)](https://badge.fury.io/py/pylocalauth)
[![Downloads](https://pepy.tech/badge/pylocalauth)](https://pepy.tech/project/pylocalauth)

---

**Documentation**: <a href="https://github.com/AppSolves/pylocalauth/blob/main/README.md" target="_blank">README</a>

**Source Code**: <a href="https://github.com/AppSolves/pylocalauth" target="_blank">Repository</a>

---

Add local authentication to your Python applications with ease. `pylocalauth` provides a simple and secure way to authenticate users using platform-specific methods such as passwords, biometrics, and PINs.

## Features

| Feature | Status |
|---------|:------:|
| **Cross-platform**: Works on Windows, macOS, and Linux. (*macOS is still in beta, but it should work reliably*) | ✅ |
| **Multiple authentication methods**: Supports password-based, biometric (Windows Hello, Touch ID, etc.), and PIN-based authentication. | ✅ |
| **Easy integration**: Simple API for integrating local authentication into your Python applications. | ✅ |
| **Secure**: Utilizes platform-specific security features to ensure user data is protected. | ✅ |
| **Lightweight**: Minimal dependencies and easy to install. | ✅ |

<br>
<p align="center">
  <kbd>
  <img src="https://raw.githubusercontent.com/AppSolves/pylocalauth/refs/heads/main/assets/usage/windows.png?sanitize=true" alt="Windows Example" width="450"/>
</kbd>
&nbsp;&nbsp;&nbsp;
<kbd>
    <img src="https://raw.githubusercontent.com/AppSolves/pylocalauth/refs/heads/main/assets/usage/linux.png?sanitize=true" alt="Linux Example" width="450"/>
  </kbd>
</p>
<br>

## Installation

You can install `pylocalauth` via pip:

```bash
pip install pylocalauth --upgrade
```

## Usage

Here's a very simple example of how to use `pylocalauth` to authenticate a user:

```python
from pylocalauth import authenticate # Import the authenticate function for your platform
result = authenticate()
if result:
    print("Authentication successful!")
else:
    print("Authentication failed.")
```

You can also customize the message displayed during authentication:

```python
from pylocalauth import authenticate
result = authenticate(message="Please authenticate to proceed.")
```

By default, `pylocalauth` will raise an `AuthUnavailableError` if authentication is not available on the current platform. You can disable this behavior by setting the `check_availability` parameter to `False` (You should only do this if you plan to handle the unavailability yourself):

```python
from pylocalauth import authenticate, is_available
from pylocalauth.exceptions import AuthError, AuthUnavailableError

# Let it handle availability automatically
try:
    result = authenticate(check_availability=True) # default
    print(f"Authentication successful?: {result}")
except AuthUnavailableError:
    print("Authentication is not available on this platform.")
except AuthError as e:
    print(f"An error occurred: {e}")

# Handle availability yourself
try:
    if not is_available():
        print("Authentication is not available on this platform.")
    else:
        result = authenticate(check_availability=False)
        print(f"Authentication successful?: {result}")
except AuthError as e:
    print(f"An error occurred: {e}")
```

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow the steps explained in the [CONTRIBUTORS](CONTRIBUTORS.md) file.

#### Contributions Needed

We are especially looking for help with the following:

- **macOS support:** Testing, bug reports, and improvements for the macOS backend.
- **Documentation & Tests:** Examples, API docs, tests (using `pytest` and `pytest-asyncio`) and usage guides.
- **CI/CD:** Enhancements to cross-platform test automation.
- **New authentication methods:** Suggestions or PRs for additional local authentication backends.
- **Issue triage:** Help us reproduce and resolve open issues.

If you want to help, please see [CONTRIBUTORS](CONTRIBUTORS.md) and open an issue or pull request!

## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply `isort` and `black` formatting:

```bash
hatch run lint
```

## License

This project is licensed under the terms of the Apache 2.0 license.
See the [LICENSE](LICENSE) file for more information.