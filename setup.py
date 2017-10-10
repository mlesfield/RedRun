from setuptools import setup

setup(
    name='redrun',
    version='0.1',
    py_modules=['runred'],
    include_package_data=True,
    install_requires=[
        'pandas', 'click',
    ],
    entry_points='''
    [console_scripts]
    runred=runred:cli
    speak=runred:speak
    ''',

)