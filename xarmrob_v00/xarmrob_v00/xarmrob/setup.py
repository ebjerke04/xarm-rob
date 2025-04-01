from setuptools import find_packages, setup
import os
from glob import glob

package_name='xarmrob'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='PeterAdamczyk',
    maintainer_email='peter.adamczyk@wisc.edu',
    description='Code for the robot arm package "xarmrob" used in the University of Wisconsin-Madison course ME/ECE 439',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'command_xarm=xarmrob.command_xarm:main',
		'cmd_sliders=xarmrob.cmd_sliders:main',
        'cmd_keyboard=xarmrob.cmd_keyboard:main'
        ],
    },
)
