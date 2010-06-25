from distutils.core import setup
import os


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('hippolyta'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:] # Strip "hippolyta/" or "hippolyta\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='django-hippolyta',
      version='0.0.1',
      description='An Amazon S3 storage backend for the Haggen website.',
      author='Peter Olsen',
      author_email='olsenpk@gmail.com',
      url='http://www.haggen.com/',
      download_url='http://code.haggen.com/',
      package_dir={'hippolyta': 'hippolyta'},
      packages=packages,
      package_data={'hippolyta': data_files},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      )
