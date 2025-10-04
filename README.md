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