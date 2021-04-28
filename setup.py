import sys
from typing import List

from setuptools import find_packages, setup


assert sys.version_info >= (3, 5, 0), "dry-pyutils requires Python 3.5+"
from pathlib import Path  # noqa E402


CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    return (
        (CURRENT_DIR / "README.md").read_text(encoding="utf8")
        + "\n\n"
        + (CURRENT_DIR / "CHANGELOG.md").read_text(encoding="utf8")
    )


def get_requirements(dev: bool = False) -> List[str]:
    file_name: str = f"requirements{'-dev' if dev else ''}.txt"

    with open(str(CURRENT_DIR.joinpath(file_name).absolute())) as f:
        install_requires = f.read().splitlines()
        if dev:
            install_requires = [
                line
                for line in install_requires
                if line and not line.startswith("-")
            ]
    return install_requires


DESCRIPTION: str = "A set of python utility methods"
GITHUB_URL: str = "https://github.com/monthero/dry-pyutils"

# Setting up
setup(
    name="DRY-python-utilities",
    version="1.0.0",
    author="Vasco Monteiro",
    author_email="vmnokk@gmail.com",
    url=GITHUB_URL,
    project_urls={
        "Changelog": f"{GITHUB_URL}/blob/master/CHANGELOG.md",
        "Instructions": f"{GITHUB_URL}/blob/master/README.md",
    },
    license="MIT",
    description="A set of python utilities",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires=">=3.5.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=get_requirements(),
    extra_requires={
        "dev": get_requirements(dev=True),
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
