from setuptools import setup, find_packages

setup(
    name="IP",
    version="0.0.1",  
    description="a convenient toolbox for image processing", 
    author="Marvin M. Doyley",  
    # author_email='author@gmail.com',
    packages=find_packages(), 
    python_requires=">=3.6",
    install_requires=['Pillow', 'matplotlib', 'numpy', 'scipy', 'scikit-image', 'scikit-learn']
)
