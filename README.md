# Python Project Template

This is a [Copier](http://copier.readthedocs.io/) template for creating new
Python projects. It provides a solid foundation with pre-configured tools and
best practices for development, testing, and deployment, helping you kickstart
your Python projects with ease.

## Usage

Ensure the following tools are available on your system. Installation guides
are linked below:

- [git](https://git-scm.com/)
- [make](https://www.gnu.org/software/make/)
- [pre-commit](https://pre-commit.com/)
- [reuse](https://reuse.software/)
- [uv](https://docs.astral.sh/uv/)

To start a new project, run the following command, replacing `<PROJECT-PATH>`
with the desired location for your new project:

```bash
uvx copier copy https://github.com/pcastellazzi/python-project.git <PROJECT-PATH>
```

This template comes with an initialization script. It will not run unless
you use the `--trust` flag with `copier`. The script is available at
<https://github.com/pcastellazzi/python-project/blob/master/post_generation.sh>
for you to review. Its purpose is to initialize the git repo. If you want to
do it manually, proceed to:

```bash
# initialize the git repo (the rest of the tooling depends on it)
git init .

# setup project (uv, pre-commit, reuse)
make setup

# the project is done, save it
git add .
git commit -m "initial commit"

# make sure everything works as expected
make check coverage integration
```

## Generated code

- `src/PACKAGE_NAME`
  This is the primary directory for your project's source code. The template
  initializes it with an empty module, serving as the root package for your
  application or library.
- `src/PACKAGE_NAME/__about__.py`
  This file stores the project's metadata, including its version, author, and
  license information, following `Hatch's` convention. It centralizes these
  details, enabling tools to easily access and modify them. For instance, you
  can automatically update the version based on the latest tag from your VCS.
  See <https://github.com/ofek/hatch-vcs>.
- `tests/`
  This directory houses the project's test suite. Using `pytest` and
  `coverage`, it ensures code quality and prevents regressions. Writing
  comprehensive tests is crucial for maintaining a robust and reliable
  project.

## Tools

- [uv](https://docs.astral.sh/uv/)
  `uv` is used for project and dependency management, ensuring isolation,
  reproducibility, and easy tool management. It streamlines the development
  workflow and helps maintain a consistent environment across different
  machines.
- [pre-commit](https://pre-commit.com/)
  This tool automates code quality checks before each commit, preventing bugs
  and enforcing code style consistency. By running linters, formatters, and
  security scanners, it helps maintain a high standard of code quality and
  reduces the risk of introducing errors. The specific hooks used are:

  - `gitleaks`
    Scans for credentials left in the repo, preventing accidental exposure of
    sensitive information.
  - `osv-scanner`
    Scans dependencies for security vulnerabilities, ensuring the project is
    protected against known exploits.
  - `reuse-tool`
    Checks for files without a declared license, ensuring compliance with
    licensing requirements.
  - `ruff-pre-commit`
    Checks for code convention violations, enforcing a consistent code style
    across the project.
  - `uv-pre-commit`
    Keeps the virtual environment and lock file up to date, ensuring
    consistent dependency versions.
- [GNU make](https://www.gnu.org/software/make/)
  While not a traditional build tool in this context, `make` is used for task
  execution, providing a convenient way to run common development tasks. The
  following targets are available:

  - `all`
    An alias for `make setup check coverage`, running the most important
    checks.
  - `check`
    Runs all `pre-commit` hooks on all files.
  - `clean`
    Removes all temporary files, using `git clean` under the hood. Be
    cautious, as uncommitted changes may be lost.
  - `coverage`
    Runs the test suite under `coverage`, generating a report in the terminal
    and the `htmlcov` folder.
  - `integration`
    Executes tests under multiple Python versions.
  - `setup`
    Creates the initial virtual environment, synchronizes dependencies,
    pre-commit hooks and licenses.
  - `test`
    Executes all tests.
  - `update-dependencies`
    Update project dependencies and `pre-commit` hooks.

## Project Settings

- `.copier-answers.yaml`
  This file stores the answers provided during the `copier` template
  generation process. It allows for future upgrades to be integrated
  seamlessly by preserving the original configuration choices.
- `.coveragerc`
  This file configures the `coverage` tool, which measures code coverage
  during testing. It specifies settings such as branch coverage, dynamic
  context, and plugins. The `covdefaults` plugin provides sensible defaults,
  while the template adjusts some values for improved reporting.
- `pyproject.toml`
  This file configures the project's build system and dependencies. It
  specifies the build backend, project metadata (name, version, description,
  etc.), and dependencies. It is the standard configuration file for Python
  projects. More information at
  <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>.
- `.python-version`
  This file specifies the default Python version used for development. It is
  used by `uv` to create a virtual environment with the correct Python
  version.
- `REUSE.toml`
  This file configures the `REUSE` tool, which helps ensure compliance with
  licensing requirements. It specifies the copyright information and license
  identifier for the project. More information at <https://reuse.software/>.
- `ruff.toml`
  This file configures the `ruff` tool, which is used for linting and
  formatting Python code. It specifies settings such as the target Python
  version, code style rules, and file exclusions. More information at
  <https://astral.sh/ruff>.
- `uv.lock`
  This file stores the resolved dependencies for the project, ensuring that
  the same versions of dependencies are used across different environments. It
  is crucial for reproducibility and should always be kept in the repository.
  More information at <https://docs.astral.sh/uv/concepts/projects/sync/>.

## Notes

- Remember to add the following to `$XDG_CONFIG_HOME/git/ignore`:
  - Your IDE configuration files (`/.vscode`, `/.idea`, etc.).
  - System specific files like `.DS_Store`.
- You can store defaults for username and email in
  `$XDG_CONFIG_HOME/copier/settings.yml`. See
  <https://copier.readthedocs.io/en/stable/settings/> for more details.
