from distutils.core import setup
setup(
    name="google_translate_api_python",
    version="1.0.0",
    description="A python wrapped free and unlimited API for Google Translate.",
    author="Ljqiii",
    author_email="ljq917181927@gmail.com",
    license="Apache-2.0",
    url="https://github.com/Ljqiii/google_translate_api_python",
    packages=["google_translate_api_python"],
    keywords=['translate','google translate api','google translate'],
    install_requires=[
        'requests',
        'PyExecJS'
    ]
)