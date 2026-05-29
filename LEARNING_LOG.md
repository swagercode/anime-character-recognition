# Learning Log

This document tracks concepts learned while building the Anime Character Recognition project.

## Project Setup

### Git repository

You initialized this folder as a Git repository and connected it to a GitHub remote.

Important terms:

- **Repository**: a folder tracked by Git.
- **Remote**: a named URL where Git can push or pull commits, commonly named `origin`.
- **Commit**: a saved snapshot of tracked file changes.
- **Working tree**: the current files on disk.
- **Clean working tree**: no uncommitted tracked or staged changes.

Checkpoint:

- What command shows whether your working tree has uncommitted changes?

Anki:

- q: What is a Git commit?
  a: A saved snapshot of tracked file changes.
- q: What is a Git remote?
  a: A named URL Git can push to or pull from, commonly named `origin`.

## Python Environment

### Virtual environment

You created a local virtual environment with `.venv`.

A virtual environment is an isolated Python installation directory for one project. It keeps this project's packages separate from packages used by other projects.

Important terms:

- **Interpreter**: the Python executable that runs your code.
- **Package**: installable Python code.
- **Dependency**: a package your project needs.
- **Editable install**: an install mode where Python imports your package from the source tree, so code edits are picked up without reinstalling.

Checkpoint:

- Is `.venv` project source code, or generated environment state?

Anki:

- q: What does `python -m venv .venv` create?
  a: A local virtual environment directory.
- q: Why ignore `.venv` in Git?
  a: It is generated environment state and can be recreated from project metadata.
- q: What does an editable install do?
  a: It installs the package so imports resolve to the source tree during development.

## Python Project Layout

### `src` layout

The project uses a `src` layout:

```text
src/
  anime_character_recognition/
    __init__.py
```

This keeps package code separate from tests, docs, and project config.

Important terms:

- **Module**: usually a single `.py` file.
- **Package**: a directory of modules, usually with `__init__.py`.
- **Import**: loading a module or name from Python code.

Checkpoint:

- Why is `anime_character_recognition` the package name but `anime-character-recognition` is the project distribution name?

Anki:

- q: What is a Python module?
  a: Usually a single `.py` file that Python can import.
- q: What is a Python package?
  a: A directory containing importable Python modules, usually marked by `__init__.py`.

## Tests

### Pytest basics

You ran `pytest`, and it found one test:

```text
tests/test_package.py
```

That test checks the package version.

Important lesson:

Passing tests only prove the behavior that the tests actually execute. The CLI previously crashed even though tests passed because no test imported or ran the CLI command path.

Checkpoint:

- Why can a project pass tests while still having a runtime bug?

Anki:

- q: What does a passing test suite prove?
  a: Only that the tested behavior passed under the tested conditions.
- q: Why did the CLI bug survive the first pytest run?
  a: The existing tests did not import or execute the CLI path.

## Command-Line Interface

### `argparse`

The project has an initial CLI module:

```text
src/anime_character_recognition/cli.py
```

It uses Python's standard-library `argparse` module to define command-line arguments.

Important terms:

- **CLI**: command-line interface.
- **Parser**: an object that knows how to read command-line arguments.
- **Subcommand**: a command inside a command, such as `classify`.
- **Required argument**: an argument the user must provide.

Important runtime behavior:

- `parse_args()` returns an `argparse.Namespace`.
- `dest="command"` controls the attribute name where the chosen subcommand is stored.
- `--image` becomes `args.image`.

Checkpoint:

- If the user runs `classify --image sample.jpg`, what value should `args.command` contain?

Anki:

- q: What does `argparse.ArgumentParser.parse_args()` return?
  a: An `argparse.Namespace`.
- q: What does `dest` control for argparse subparsers?
  a: The attribute name used on the returned `Namespace`.
- q: Why does `--image` become `args.image`?
  a: `argparse` converts the option name into a valid Python attribute name.

## Runtime Errors

### `NameError`

The CLI previously tried to print a name that did not exist:

```text
classification
```

Python raised a `NameError` because it could not find that name in the active scopes.

Important terms:

- **Name**: an identifier like `classification`, `args`, or `parser`.
- **Scope**: the region where a name can be looked up.
- **NameError**: an exception raised when Python cannot find a requested name.

Checkpoint:

- Why is printing a clear "not implemented" message better than referencing a variable that does not exist?

Anki:

- q: What is a Python `NameError`?
  a: An exception raised when Python cannot find a requested name.
- q: What is a scope?
  a: A region where Python can look up names.

## Computer Vision Goal

### First project target

The first version of this project should be image classification:

```text
input image -> one character label
```

Important terms:

- **Image classification**: predicting one label for an image.
- **Dataset**: examples used for training and evaluation.
- **Label**: the correct answer for an example.
- **Validation set**: examples held back to estimate performance on unseen data.
- **Transfer learning**: adapting a pretrained model to a smaller project-specific dataset.

Important project trap:

If all images of one character share the same background, the model may learn the background instead of the character.

Checkpoint:

- Why is background variety important when collecting character images?

Anki:

- q: What is image classification?
  a: A computer vision task where a model predicts one label for an image.
- q: What is a label in supervised learning?
  a: The correct answer attached to a training example.
- q: What is transfer learning?
  a: Using a pretrained model and adapting it to a new task.
- q: Why can repeated backgrounds hurt image classification?
  a: The model may learn the background as a shortcut instead of the target object or character.
