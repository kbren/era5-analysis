"""Sphinx configuration."""
project = "Era5 Analysis"
author = "Katie Brennan"
copyright = "2024, Katie Brennan"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
