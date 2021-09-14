#!/bin/bash
export virtualMode="on"
export debugMode="on"
cd web/front
npm run build
cd ../../
python3 main.py