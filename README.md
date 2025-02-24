# E-commerce
by lolomyn

## Description:

электронная торговля, или электронная коммерция

## Install:

**Ubuntu**

`sudo apt update` - update all packages

- python

`sudo apt install python3` - install python

`python3 -V` - check python version

- git

`sudo apt install git` - install git

`git --version` - check git version

- poetry

`sudo apt install python3-poetry` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/skypro_oop.git`

- install dependencies

`poetry add requests`

- start

`python3 main.py`

**Windows**

`sudo apt update` - update all packages

- python

Download it  [here](https://www.python.org/) and follow instructions

`python --version` - check python version

- git

Download in [here](https://git-scm.com/) and follow instructions

`git --version` - check git version

- poetry

`curl -sSL https://install.python-poetry.org | python -` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/skypro_project_1.git`

- install dependencies

`poetry add requests`

- start

`python main.py`

## Functional

### Class Product
    name: str
    description: str
    price: float
    quantity: int

Содержит информацию о продуктах

#### Subclass Smartphone
    Product(name: str, description: str, price: float, quantity: int)
    efficiency: float
    model: str
    memory: int
    color: str

Дочерний класс, содержащий информацию о характеристиках смартфона

#### Subclass Lawngrass
    Product(name: str, description: str, price: float, quantity: int)
    country: str
    germination_period: str
    color: str

Дочерний класс, содержащий информацию о характеристиках газона

### Class Category
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

Содержит информацию о категориях, их количестве и количестве продуктов в категориях    
    

    
    