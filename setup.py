from setuptools import setup

setup(name='sharelockUtils',
      version='0.2',
      description='Simple utils for Sharelock',
      url='',
      author='Rani',
      author_email='rani@snip.today',
      license='MIT',
      packages=['sharelock_utils'],
      install_requires=[
            "sqlalchemy>=1.2.0",
        ],
      classifiers=['Programming Language :: Python :: 3.6'],
      zip_safe=False)