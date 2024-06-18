# Receipt Recognition System

## Introduction
The receipt recognition system is designed to accurately recognize and extract information from receipt images. This project separates the products on the receipts, allows each user to distinguish them by category and shows how much money he spent on which category by month.

## Installation
To install the necessary dependencies, run the following commands:

```bash
git clone https://github.com/VahagnSyan/receipt-recognition-system.git
cd receipt-recognition-system
poetry install
npm install
```

## Benchmarks


| 2.jpg | 9.jpg | 12.jpg | 15.jpg | 50.jpg |
| :-----| :-----| :-----| :-----| :-----|
| 80%   | 76.4% | 91%   | 95%   | 97%   |


- [More Tested receipts images and results](https://drive.google.com/drive/folders/1Je9ydDAXDeL3wAAqWh6y9gSRAXtg896B?usp=sharing)


## Folder structure
```
.
├── client
│   ├── index.html
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── public
│   │   ├── images
│   │   │   └── folder-icon.png
│   │   └── vite.svg
│   ├── README.md
│   ├── src
│   │   ├── App.tsx
│   │   ├── components
│   │   │   ├── AuthForm
│   │   │   │   └── AuthForm.tsx
│   │   │   ├── Header
│   │   │   │   └── Header.tsx
│   │   │   ├── Layout
│   │   │   │   └── Layout.tsx
│   │   │   ├── Loader
│   │   │   │   └── Loader.tsx
│   │   │   ├── ProductsList
│   │   │   │   ├── ProductsList.tsx
│   │   │   │   ├── ProductsRenderer.tsx
│   │   │   │   └── Product.tsx
│   │   │   ├── Screens
│   │   │   │   ├── Dashboard
│   │   │   │   │   └── index.tsx
│   │   │   │   ├── Home
│   │   │   │   │   └── Home.tsx
│   │   │   │   ├── Profile
│   │   │   │   │   ├── Profile.tsx
│   │   │   │   │   └── Sidebar
│   │   │   │   │       └── Sidebar.tsx
│   │   │   │   ├── SignIn
│   │   │   │   │   └── SignIn.tsx
│   │   │   │   └── SignUp
│   │   │   │       └── SignUp.tsx
│   │   │   └── UploadImageWidget
│   │   │       └── UploadImageWidget.tsx
│   │   ├── images
│   │   │   └── Images.ts
│   │   ├── index.css
│   │   ├── main.tsx
│   │   ├── services
│   │   │   └── authentication.ts
│   │   ├── types
│   │   │   └── index.ts
│   │   ├── utils
│   │   │   └── index.ts
│   │   └── vite-env.d.ts
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
├── images
│   ├── 12.jpg
│   ├── 15.jpg
│   ├── 2.jpg
│   ├── 50.JPG
│   └── 9.jpg
├── README.md
└── server
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   ├── analytics
    │   │   ├── analytics.py
    │   │   └── __pycache__
    │   │       └── analytics.cpython-310.pyc
    │   ├── authentication
    │   │   ├── authentication.py
    │   │   └── __pycache__
    │   │       └── authentication.cpython-310.pyc
    │   ├── client_image_processing
    │   │   ├── add_purchases.py
    │   │   ├── image_processing.py
    │   │   └── __pycache__
    │   │       ├── add_purchases.cpython-310.pyc
    │   │       └── image_processing.cpython-310.pyc
    │   ├── db
    │   │   └── connect_db.py
    │   ├── extraction
    │   │   ├── extraction.py
    │   │   └── __pycache__
    │   │       ├── detection.cpython-310.pyc
    │   │       └── extraction.cpython-310.pyc
    │   ├── images
    │   │   └── result.png
    │   ├── main.py
    │   ├── postprocessing
    │   │   ├── post_processing.py
    │   │   └── __pycache__
    │   │       └── post_processing.cpython-310.pyc
    │   ├── preprocessing
    │   │   ├── preprocessing.py
    │   │   └── __pycache__
    │   │       ├── post_processing.cpython-310.pyc
    │   │       └── preprocessing.cpython-310.pyc
    │   ├── recognition
    │   │   ├── __pycache__
    │   │   │   └── recognition.cpython-310.pyc
    │   │   └── recognition.py
    │   └── utils
    │       ├── __pycache__
    │       │   └── utils.cpython-310.pyc
    │       └── utils.py
    └── tests
        └── __init__.py
```
