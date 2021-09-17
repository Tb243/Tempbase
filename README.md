# Tempbase

## Setting up the web server

You need to install a Python websocket server library.

```bash
pip3 install --user git+https://github.com/Pithikos/python-websocket-server
```

## Setting up the web front-end

You will need to install a recent version of [Node.js](https://nodejs.org). Afterwards, simply execute the following to install package dependencies

```bash
cd src/web/front
npm i
```

You can now run the front-end build system.

__To run the build system in watch mode__

```bash
npm run start
```

__To build for production mode__

```bash
npm run build
```

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

__Setting up SMS:__

//Documentation: https://www.twilio.com/docs/sms/quickstart/python#install-python-and-the-twilio-helper-library//

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew tap twilio/brew && brew install twilio
pip install twilio
```