# Hardware Abstraction Layer

The HAL should provide the overall application a predictable way to access the physical components of the device. In addition to this, each physical device should have a "virtual" device that simulates the hardware, allowing developers without hardware to reliably develop and test the software.

## Testing the devices

Run `python3 test_devices.py`. If you are running on Raspbian, this should also test physical devices automatically.

## Example usage 

See `example.py`