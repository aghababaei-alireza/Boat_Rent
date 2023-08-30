from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name = 'Boat_Rent',
    version = '1.0.0',
    author = 'Alireza Aghababaei, Majid Montazeri, Rasoul Dashti, MohammadReza Mohammadi, Shohre Shahsavari, Shivana Fallahi, Sonia Imani',
    author_email = 'aghababaei1375@gmail.com',
    description = 'سامانه مدیریت دریاچه و اجاره قایق',
    python_requires='>=3.10',
    packages=["Core", "UI"],
    install_requires = required
)