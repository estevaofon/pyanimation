from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pyanimation',
      version='0.3',
      description='A pygame animation package',
      long_description=long_description,
      author='Estevao Fonseca',
      author_email='estevaopfon@gmail.com',
      license='MIT',
      url='https://github.com/estevaofon/pyanimation',
      packages=['pyanimation'],
      download_url='https://github.com/estevaofon/pyanimation/archive/0.3.tar.gz',
      install_requires=['pygame'],
      keywords=['pygame', 'animation', 'pyanimation'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',
          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',
          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      )
