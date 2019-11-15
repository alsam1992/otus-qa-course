from setuptools import setup, find_packages

setup(name='otus-qa',
      version='0.1',
      url='https://github.com/alsam1992/otus-qa-course',
      license='MIT',
      author='alsam1992',
      author_email='alsam1992@yandex.ru',
      description='Otus qa python code',
      packages=find_packages(exclude=['tests']),
      setup_requires=['pytest'],
      zip_safe=False)

