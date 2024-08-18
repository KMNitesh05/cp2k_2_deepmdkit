from setuptools import setup, find_packages

setup(
    name='cp2k_2_deepmdkit',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'c2d-coord=cp2k_to_deepmdkit.coord:main',
            'c2d-force_energy=cp2k_to_deepmdkit.force_energy:main',
            'c2d-box=cp2k_to_deepmdkit.box:main',
            'c2d-convert=cp2k_to_deepmdkit.convert:main',
        ],
    },
    install_requires=[],
)