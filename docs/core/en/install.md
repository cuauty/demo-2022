# All-scale Causal Engine Installation Guide

Open-ACE currently primarily provides its functionality through images, encompassing both compilation and runtime environments.

## Docker Image

```
openasce/asce:gcc9.4-py3.11
```

The image contains all the dependencies required to run Open-ACE. Users no longer need to worry about environment configuration within the Docker container.

## Installation Steps

### 1. Clone the code

```
git clone https://github.com/Open-All-Scale-Causal-Engine/OpenASCE.git
```

### 2. Start Docker

```
docker pull openasce/asce:gcc9.4-py3.11
docker run --net=host --rm -it -m 16g --name openasce_env open-asce/asce:gcc9.4-py3.11 "/bin/bash"
```

### 3. Compile the Source Code

```
bash scripts/build.sh
```

By executing this script, the package will be compiled based on the current branch and installed in the current Docker, replacing any existing installation. The package can be found in the dist directory and is typically named openasce-0.1-py3-none-any.whl and openasce-0.1.tar.gz.
