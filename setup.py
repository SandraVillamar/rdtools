#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    raise RuntimeError('setuptools is required')


import versioneer


DESCRIPTION = 'Functions for reproducible timeseries analysis of photovoltaic systems.'

LONG_DESCRIPTION = """
RdTools is an open-source library to support reproducible technical analysis of
PV time series data. The library aims to provide best practice analysis
routines along with the building blocks for users to tailor their own analyses.

Source code: https://github.com/NREL/rdtools
"""

DISTNAME = 'rdtools'
LICENSE = 'MIT'
AUTHOR = 'Rdtools Python Developers'
AUTHOR_EMAIL = 'RdTools@nrel.gov'
MAINTAINER_EMAIL = 'RdTools@nrel.gov'

URL = 'https://github.com/NREL/rdtools'

SETUP_REQUIRES = [
    'pytest-runner',
]

TESTS_REQUIRE = [
    'pytest >= 3.6.3',
]

INSTALL_REQUIRES = [
    'matplotlib >= 2.2.2',
    'numpy >= 1.12',
    'pandas >= 0.23.0,!=1.0.0,!=1.0.1',  # exclude 1.0.0 & 1.0.1 for GH142
    'statsmodels >= 0.8.0',
    'scipy >= 0.19.1',
    'h5py >= 2.7.1',
    'pvlib >= 0.7.0, <0.8.0',
    'plotly>=4.10.0',
    'scikit-learn >= 0.24.1',
    'joblib >= 1.0.1'
]

EXTRAS_REQUIRE = {
    'doc': [
        'sphinx==1.8.5',
        'nbsphinx==0.4.3',
        'nbsphinx-link==1.3.0',
        'pandas==0.23.0',
        'pvlib==0.7.1',
        'sphinx_rtd_theme==0.4.3',
        'ipython',
    ],
    'test': [
        'pytest',
        'coverage',
    ]
}
EXTRAS_REQUIRE['all'] = sorted(set(sum(EXTRAS_REQUIRE.values(), [])))


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering',
]

KEYWORDS = [
    'photovoltaic',
    'solar',
    'analytics',
    'analysis',
    'performance',
    'degradation',
    'PV'
]

setuptools_kwargs = {
    'zip_safe': False,
    'scripts': [],
    'include_package_data': True
}

# set up packages to be installed and extensions to be compiled
PACKAGES = ['rdtools']


setup(name=DISTNAME,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      packages=PACKAGES,
      keywords=KEYWORDS,
      setup_requires=SETUP_REQUIRES,
      tests_require=TESTS_REQUIRE,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer_email=MAINTAINER_EMAIL,
      license=LICENSE,
      url=URL,
      classifiers=CLASSIFIERS,
      **setuptools_kwargs)
