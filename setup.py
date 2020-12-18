from distutils.core import setup

VERSION = '1.0.0'

setup(
  name = 'body_measurements',
  packages = ['body_measurements'], # this must be the same as the name above
  version = VERSION,
  description = 'It allows us to measure the human body generated by SMPL model.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Carlos Roca',
  author_email = 'u2carlosroca@gmail.com',
  url = 'https://github.com/vcarlosrb/3d-body-measurements', # use the URL to the github repo
  download_url = 'https://github.com/vcarlosrb/3d-body-measurements/tarball/0.1',
  keywords = ['body', 'measurements', 'SMPL'],
  python_requires=">=3.8",
  install_requires = [
    "trimesh>=3.8.8",
    "numpy>=1.19.1",
    "scipy>=1.5.2",
    "shapely>=1.7.1",
    "networkx>=2.5"
  ]
)