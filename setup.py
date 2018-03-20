from setuptools import setup, find_packages

setup(name='morphsnakes',
      version='1.0',
      description='Git Repo for morphsnakes algorithm',
      author='P. Márquez Neila <p.mneila@upm.es>',
      package_dir={'':'src'},
      packages=find_packages('src'),
      install_requires=['numpy', 'scipy']
)
