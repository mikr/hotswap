from distutils.core import setup
import hotswap

params = {
    'name':         'hotswap',
    'version':      hotswap.version,
    'description':  hotswap.__doc__.splitlines()[0],
    'long_description': hotswap.__doc__,
    'author':       hotswap.__author__,
    'author_email': hotswap.__email__,
    'license':      'MIT License',
    'url':          'http://www.krause-software.de/python/index.html',
    'classifiers':  [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    'py_modules':   ['hotswap'],
}

setup(**params)
