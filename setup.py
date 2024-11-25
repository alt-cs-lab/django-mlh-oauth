from setuptools import setup, find_packages

setup(
    name='django_mlh_oauth',  # package import name
    version='0.1',
    packages=['django_mlh_oauth'],
    include_package_data=True,
    install_requires=[
        'django>=5',  # package requires django 5
        
    ],
    description='django package for auth using KSU cas server',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alt-cs-lab/django-mlh-oauth',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10',  # package requires python 3.10
)
