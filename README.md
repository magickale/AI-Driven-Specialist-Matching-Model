# How to setup Project Environment

## 1. Install and activate Python 3.10 with pyenv
```shell
pyenv install 3.10
pyenv shell 3.10
python3 --version
```

Verify you are now on python 3.10

## 2. Install Project Dependencies
```shell
python3 -m pip install --upgrade pip setuptools wheel packaging
python3 -m pip install torch==2.1.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
python3 -m pip install git+https://github.com/NVIDIA/NeMo.git@r2.0.0rc0#egg=nemo_toolkit[nlp]
```

Your environment is now setup!
