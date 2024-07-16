<h1 align="center" style="margin-top: 0px;">uvl-spellchecker</h1>

# Describtion
This microservice provides the functionality to create a spellchecked dataset based on an existing dataset. For spellchecking, [LanguageTool](https://languagetool.org/de) is used.

# Requirements

## Hardware

## Software
- >=Python 3.11
- java runtime 8.0 or higher

# Getting Started as containerized microservice

```sh
docker build -t <CONTAINER_NAME> -f "./Dockerfile" .

docker run -p 9699:9699 --name sc sc
```

# Local Network
```sh
docker build --no-cache -t sc -f "./Dockerfile" --network host .

docker run --network host -p 9699:9699 --name sc sc
```

# Getting Started as local testing
## 1. Clone the repository

```sh
git clone https://github.com/feeduvl/uvl-spellchecker.git
cd uvl-spellchecker
```

## 2. Create a virtual environment (optional)

### venv
...

### conda

**1. conda installation:**
[Installation of miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install)

**2. conda activation:**
```sh
conda create -n sc python=3.11
conda activate sc
```

## 3. Setting up the development environment

```sh
cd <THE_BASE_DIRECTORY_FOR_THE_uvl-spellchecker_SERVICE>
pip install -e .
```

## 4. Start the uvl-spellchecker service
```sh
./start.sh
```
