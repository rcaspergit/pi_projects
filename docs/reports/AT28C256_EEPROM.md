# Table of contents
  1. [Purpose](#purpose)
  2. [Abstract](#abstract)
  3. [Removing write lock](#Write_Lock)

## Purpose <a name="purpose"></a> :
To develop the code to support reads and write to the AT28C256 EEPROM for use with the 6502 microprocessor the build up components necessary to run code on the 6502.

## Abstract <a name="abstract"></a> :
This activity had several chalanges. The AT28256 chip was purchased "new" but like many of the chips purchased, this chip had data on it. while attempting to clear the data it was determined that the chip was also write locked. Since the chip ises 5 volts for both reads and writes, there is a risk of accidental wwrites when the system is power up. If the write enable, output enable, and chip enable pins come up in the "write state", whatever is on the dat lines and address lines will be written to the chip. To prevent this the chip has a write lock capability the prevents accidental writes but either preventing all writes or writs that are not prefixed with a wpecific write code. The write lock can be removed but sending a specific pattern to the chip. there are very specific timing requirements for the unlock process and these will be documented here.

Once the unlock is process is succesfully performed the chip will be programmed with a simple assembly program that will loop and be used to light up a set of LED's with a easily verifiable pattern.

## Removing Write Lock <a name="Write_Lock"></a> :

A detailed explaination of the Write lock capability and procedures for setting and clearing the lock can be reviewed [here](https://github.com/rcaspergit/pi_projects/blob/master/docs/datasheets/AT28C256_datasheet.pdf).

The process taken from the data sheet is [](https://github.com/rcaspergit/pi_projects/blob/master/docs/images/memory/AT28C256/Write_lock_process.png)
