# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OHIS Radio KISS'
copyright = '2025, un-Creatrix'
author = 'un-Creatrix'
github_url = 'https://github.com/un-creatrix/OHIS-Radio_KISS'

release = '0.0'
version = '0.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': '#FF7BAC',
    'flyout_display': 'hidden',
    'version_selector': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = 'footnote'
