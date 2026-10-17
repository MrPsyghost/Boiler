# Boiler

**A project template manager for developers.**

Boiler helps you create, store, manage, and reuse project templates directly from your terminal. Stop setting up the same project structure repeatedly — create a template once and reuse it whenever you need it.

```text
██████╗  ██████╗ ██╗██╗     ███████╗██████╗
██╔══██╗██╔═══██╗██║██║     ██╔════╝██╔══██╗
██████╔╝██║   ██║██║██║     █████╗  ██████╔╝
██╔══██╗██║   ██║██║██║     ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║███████╗███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
```

> **Current version:** `0.0.1 (beta)`

## Features

- **Template management** — Create, list, use, and remove project templates.
- **Quick project initialization** — Set up a project using a saved template.
- **Add existing files** — Add files and directories to a template.
- **Template selection** — Select a template to work with.
- **Command-line interface** — Manage everything directly from your terminal.
- **Configurable appearance** — Customize the banner, colors, and other settings through `boiler.cfg`.
- **Windows executable** — Run Boiler from your terminal after installation.
- **UPI donations** — Generate a donation QR code directly in the terminal.

## Installation

### Windows installer

1. Download the Boiler installer from the project's [GitHub Releases](https://github.com/MrPsyghost/Boiler/releases) page.
2. Run the installer.
3. Follow the installation instructions.
4. Open a new PowerShell or Command Prompt window.

Verify the installation:

```powershell
boiler -v
```

Display the available commands:

```powershell
boiler -h
```

**Note:** The installer should add Boiler's installation directory to your system `PATH`. Open a new terminal after installation so Windows can recognize the updated environment.

## Getting started

### 1. Create a template

Create a template with your desired name:

```powershell
boiler boil -n <NAME>
```

### 2. Add files to a template

Add a file or directory to a template:

```powershell
boiler add <FILE> -n <NAME>
```

You can also add a directory:

```powershell
boiler add <DIRECTORY> -n <NAME>
```

Or add multiple files or directories:

```powershell
boiler add . -n <NAME>
```

The `-n` or `--name` option specifies the template to modify. If the command supports selecting a template through another mechanism, select the appropriate template first.

You can also set a current template so you don't have to specify its name repeatedly:

```powershell
boiler set -n <NAME>
```

By default, Boiler automatically sets a newly created template as the current template.

### 3. List your templates

```powershell
boiler list
```

Example output:

```text
1. pygame
2. template1
3. flask
```

### 4. Initialize a project

Use a saved template to create a project in your current working directory:

```powershell
boiler init -n <NAME>
```

Follow any prompts to select a template, if required.

### 5. Remove a template

```powershell
boiler remove -n <NAME>
```

To remove all templates:

```powershell
boiler remove -a
```

Boiler may ask for confirmation before deleting templates. **Bulk removal is destructive**, so make sure you have backups of any important data before confirming.

## Commands

| Command | Description |
| --- | --- |
| `boiler boil` | Create a new template |
| `boiler init` | Initialize a project from a template |
| `boiler set` | Set or update a template-related setting |
| `boiler add` | Add files or directories to a template |
| `boiler clear` | Clear template contents or the currently selected template, depending on the implementation |
| `boiler list` | List available templates |
| `boiler remove` | Remove a template or all templates |
| `boiler path` | Display a path to where templates exist |
| `boiler donate [AMOUNT]` | Generate a UPI donation QR code in the terminal |
| `boiler --help` | Display help information |
| `boiler --version` | Display version information |

### Options

| Option | Description |
| --- | --- |
| `-h`, `--help` | Display the help message |
| `--version` | Display version information |
| `-n NAME`, `--name NAME` | Specify a template name |
| `-a`, `--all` | Remove all existing templates |

To view the syntax supported by your installed version, run:

```powershell
boiler -h
```

## Configuration

Boiler uses a `boiler.cfg` configuration file.

Example:

```ini
name=Boiler
version=0.0.1
versionType=beta
description=Project template manager for developers
author=MrPsyghost
license=MIT
asciiFont=ANSI_Shadow
color=light_yellow
showBanner=true
```

| Setting | Purpose |
| --- | --- |
| `name` | Application name |
| `version` | Release version |
| `versionType` | Release type, such as `beta` |
| `description` | Short application description |
| `author` | Project author |
| `license` | Project license |
| `asciiFont` | ASCII banner font |
| `color` | Banner color |
| `showBanner` | Determines whether the banner is displayed |

The configuration file is distributed with the application. User-specific templates and mutable settings should be stored in the user's application data directory rather than in the protected installation directory.

For donations, configure the following settings in `boiler.cfg`:

```ini
donationUPI=your-upi-id
donationName=Your Display Name
donationMessage=Support Boiler
```

Replace the example values with your own details. Donations are optional, and the QR code contains the payment details needed to initiate a UPI payment.

## Development

Want to contribute to Boiler or build it from source? Follow the instructions below.

### Requirements

- Python
- GNU Make (optional; you can also build the project manually)
- PyInstaller
- Inno Setup 6 (to compile the Windows installer)

### Set up the project

Clone the repository:

```powershell
git clone https://github.com/MrPsyghost/Boiler.git
cd Boiler
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies using the project's dependency file, including Segno for terminal QR-code generation.

### Build the executable

```powershell
make build
```

The executable should be generated at:

```text
dist/boiler.exe
```

### Build the installer

After building the executable, make sure Inno Setup 6 is installed and correctly configured.

Run:

```powershell
make installer
```

## Project structure

A simplified view of the project:

```text
Boiler/
├── src/
│   ├── main.py
│   ├── boiler.cfg
│   ├── boiler.ico
│   └── ...
├── compiler.iss
├── Makefile
├── README.md
└── dist/
    ├── boiler-setup-v(VERSION)-(VERSION-TYPE).exe
    ├── boiler.exe
    └── boiler.cfg
```

The exact project structure may vary as development continues.

## Roadmap

Boiler is currently in beta. Potential future improvements include:

- Improved template management and selection.
- More robust error handling during file operations.
- Better cross-platform support.
- Additional configuration options.
- A smoother release and update workflow.

## Issues and feedback

Found a bug or have an idea for a new feature?

Open an issue on the [Boiler GitHub repository](https://github.com/MrPsyghost/Boiler/issues).

Please include the command you ran, the expected behavior, the actual behavior, and any relevant error messages.

## Supporting Boiler

You can support Boiler with a voluntary UPI donation.

Generate a donation QR code for a specific amount in INR:

```powershell
boiler donate 50
```

Or run the command without an amount to enter one interactively:

```powershell
boiler donate
```

Scan the QR code using a compatible UPI app to initiate the payment. Boiler does not currently verify whether a payment was completed, so its thank-you message should not be treated as payment confirmation.

## License

Boiler is released under the **MIT License**.

See the `LICENSE` file for the full license text.

## Author

### MrPsyghost

- Portfolio: [MrPsyghost Portfolio](https://mrpsyghost.onrender.com/)
- GitHub: [MrPsyghost GitHub](https://github.com/MrPsyghost)

---

*Build once. Reuse everywhere. Stay productive with Boiler.*
