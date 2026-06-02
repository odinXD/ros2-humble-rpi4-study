from setuptools import find_packages, setup

package_name = 'py_practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='doyeong',
    maintainer_email='dlehdud85@naver.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = py_practice.publisher_node:main',
            'subscriber_node = py_practice.subscriber_node:main',
            'status_publisher = py_practice.status_publisher:main',
            'status_subscriber = py_practice.status_subscriber:main',
        ],
    },
)
