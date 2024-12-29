#!/usr/bin/env python3

"""A module to install the discord_message_channel program, in order to send notifications from within python programs.
The message_channel file must be edited as shown in the readme file BEFORE installation.
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
	name="discord_message_channel",  
	version="1.0.0", 
	description="A python add-on to allow discord notifications to be sent from within python code and projects.", 
	url="https://github.com/aerynsfyre/discord_message_channel", 
	author="Aeryn Dunmore",  
	author_email="aeryn@dunmore.nz",  
	classifiers=[ 
		"Development Status :: 2 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Program Aid :: Coding Tools :: Messaging :: Discord :: Program Notifications",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3 :: Only",
	],
	keywords="messaging, codingtools, programnotifications, discord, development",  
	py_modules=["discord_message_channel"],
	#
	packages=find_packages(where="src"), 
	python_requires=">=3.7, <4",
	install_requires=["requests"],

)