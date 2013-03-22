from setuptools import setup, find_packages

setup(
    name='jmbo-everlytic',
    version='dev',
    description='Jmbo Everlytic mailing list subscription API.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt International',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-everlytic',
    packages = find_packages(),
    dependency_links = [
        'http://github.com/praekelt/jmbo-foundry/tarball/develop/2.6.praekelt#egg=jmbo-foundry-2.6.praekelt',
    ],
    install_requires = [
        'lxml',
        'xmlrpclib',
        'jmbo-foundry==1.1.15',
        'django>=1.4,<1.5',
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
