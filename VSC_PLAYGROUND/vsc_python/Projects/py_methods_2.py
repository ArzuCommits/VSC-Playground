import string
import random
import pywhatkit
import math
import time
import datetime
import os
import faker
import sys
import statistics
import pandas
import tkinter
import numpy
import pygame
import logging
import json
import discord
import calendar
import email
import forex_python.converter
import winsound
import shutil
import pypdf 
import win32com.client
import requests
import bs4
import re
import googletrans
import functools
import importlib

def method(user_input):
    user = importlib.import_module(user_input)

    methods = dir(user) 

    i = 0

    for  method in methods:
        if '__' not in method:
            i+=1
            return f"{i}: {method}" 

