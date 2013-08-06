from setuptools import setup, find_packages

VERSION = (0, 6, 1)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

setup(
    name = 'django-colissimo',
    version = version,
    description = "Django app to get shipping prices from La Poste Colissimo",
    long_description = """django-colissimo provides the ability to get prices from the La Poste Colissimo postal service.""",
    author = 'Mathias Monnerville',
    author_email = 'mathias@monnerville.com',
	url = 'https://github.com/matm/django-colissimo',
    license = 'GPL 3',
    platforms = ['any'],
    classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU General Public License (GPL)',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Framework :: Django'],
    packages = find_packages(),
    setup_requires=["setuptools_hg"],
    include_package_data = True,
)

