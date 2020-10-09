#!/usr/bin/env python3

"""Main class for the Lightning ATM

Refactoring of the original project by 21isenough -- Thanks!
"""

# Requirements
import logging
import configparser
import argparse


class LightningATM:
    """Class for LightningATM; this is where the magic happens"""


def main():
    """Run the main class"""
    argumentparser = argparse.ArgumentParser()
    argumentparser.add_argument("--debug", help="Set console logging to debug",action="store_true")
    argumentparser.add_argument("--configfile", help="Path to config file",default="~/.lightningATM/config.ini")
    arguments=argumentparser.parse_args()

    print(arguments.configfile)



    # Set up logging first
    
    # Initialize the ATM
    atm=LightningATM()


if __name__ == "__main__":
    main()


