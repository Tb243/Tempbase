#!/bin/bash
export virtualMode="off"
export debugMode="off"
cd web/front
npm run build
cd ../../
python3 main.py