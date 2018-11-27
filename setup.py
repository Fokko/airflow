import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airflow",
    version="0.0.1",
    author="Apache Author",
    author_email="dev@airflow.incubator.apache.org",
    description="Placeholder for the old Airflow package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apache/incubator-airflow",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Monitoring',
    ],
)

def do_setup():
    raise RuntimeError('Please install package apache-airflow instead of airflow')

if __name__ == "__main__":
    do_setup()
