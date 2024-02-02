# streamlit-ml
Streamlit app to serve ML services


## Get started

1. Create and source venv

Using Conda:
```bash
$ conda env create -f environment.yml
& conda activate myenv
```

2. Install requirements:

Using Make:
```
$ make install
```

Using pip:
```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

## Run app locally

1. Navigate to the app folder.
```bash
$ cd app
```

2. Run app:
```bash
python -m streamlit run app.py
```