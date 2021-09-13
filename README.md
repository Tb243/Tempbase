# Tempbase

## Running unit tests

Unit tests are available for virtual and physical devices in the hardware abstraction layer. Physical devices will only be loaded
if the the required hardware libraries are installed.

```bash
cd src
python3 test_devices.py
```

## Running the main service

The main entry point of the service is `src/main.py`. Production mode can be run using

```bash
cd src
python3 main.py
```

Environment variables can also be to control virtual device mode and debug logging messages. The available environment variables are

```
virtualMode [off|on]
debugMode [off|on]
```

## Using the bash runner scripts

To simplify the environment variables, two bash runner scripts exist. 

__Virtual devices, debugging turned on:__

```
cd src
./run-virtual.sh
```

__Physical devices, debugging turned off:__

```
cd src
./run-physical.sh
```