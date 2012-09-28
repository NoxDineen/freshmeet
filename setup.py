try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='freshmeet',
    version=0.1,
    description='',
    author='',
    author_email='',
    url='',
    install_requires=[
        'flask == 0.9',
        'pysqlite == 2.6.3'
    ]
)