import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version_namespace = {}
with open('picam_vps/version.py') as f:
    exec(f.read(), version_namespace)


def package_files(*dirs):
    paths = []
    for d in dirs:
        for (path, directories, filenames) in os.walk(d):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('picam_vps/resources')
setup_deps = [
                 'wheel',
                 'twine'
             ],

setup(name='picam-vps',
      version=version_namespace['__version__'],
      description='Picam VPS',
      long_description=long_description,
      classifiers=[],
      url='https://github.com/vossenv/picam-vps',
      maintainer='Danimae Vossen',
      maintainer_email='vossen.dm@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'click',
          'click-default-group',
          'pyyaml',
          'schema',
          'distro',
          'requests',
          'numpy==1.18',
          'imutils',
      ],
      extras_require={
          ':sys_platform=="win32"': [
              'opencv-python',
          ],
          'setup': setup_deps,
      },
      setup_requires=setup_deps,
      entry_points={
          'console_scripts': [
              'picam-vps = picam_vps.app:cli',
          ]
      },
      )
