# How to setup Project Environment

## 1. Install and activate Python 3.10 with pyenv
```shell
pyenv install 3.10
pyenv shell 3.10
python3 --version
```

Verify you are now on python 3.10

## 2. Create a virtual environment (optional)
```shell
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Project Dependencies
```shell
python3 -m pip install --upgrade pip setuptools wheel packaging
python3 -m pip install torch==2.1.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
python3 -m pip install cython
python3 -m pip install psutil
python3 -m pip install "huggingface_hub==0.19.4"
python3 -m pip install --no-build-isolation youtokentome
python3 -m pip install "nemo_toolkit[nlp]==1.21.0"
```

Your environment is now setup!
