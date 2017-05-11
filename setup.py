from setuptools import setup

setup(
    name='kmer_sniper',
    version='1.0',
    packages=[],
    url='',
    license='',
    install_requires=[ 'numpy', 'biopython', 'requests', 'pysam', 'intervaltree'],
    author='Keith Simmon',
    author_email='keith.simmon@aruplab.com',
    description='returns kmer counts for sequence regions',
    package_data={'kmer_sniper' : ['resources/*.txt', 'resources/*.gz']},
)
