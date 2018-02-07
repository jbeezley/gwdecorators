from setuptools import setup, find_packages

setup(name='gwtasks-demo',
      version='0.0.1',
      description='A package for experimenting with gw decorators using click',
      entry_points={
          'girder_worker_plugins': [
              'gwtasks-demo = gwtasks_demo:GWTaskDemoPlugin',
          ]
      },
      install_requires=['click', 'girder_worker', 'girder_worker_utils'],
      packages=find_packages())
