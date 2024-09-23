import os
import requests
import argparse
import time
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument("-track", "-t", type=str, help="Enter an IP address to get information.")
parser.add_argument("-trackme", "-tm", action='store_true', help="Get information about your own IP.")
args = parser.parse_args()

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def locate(ip):
    print(f'[~] Searching for data on: {ip}')
    time.sleep(1)
    api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=en"

    data = requests.get(api).json()
    ##-----------Query---------##
    print("\n[~] [IP]:", data['query'])
    ##--------------ISP-----------##
    try:
        print("[~] [ISP] :", data['isp'])
        if data['isp'] == False:
            print('[~] [ISP not found!]')
        ##------------Org-----------##
        print("[~] [Organization]:", data['org'])
        if data['org'] == False:
            print('[~] [Organization not found!]')
        ##-----------City---------##
        print("[~] [City]:", data['city'])
        if data['city'] == False:
            print('[~] [City not found!]')
        ##-----------Country---------##
        print("[~] [Country Name]:", data['country'])
        if data['country'] == False:
            print('[~] [Country name not found!]')
        ##----------Region-------##
        print("[~] [Region]:", data['region'])
        if data['region'] == False:
            print('[~] [Region not found!]')
        ##---------Continent Name---##
        print("[~] [Continent Name]:", data['continent'])
        if data['continent'] == False:
            print('[~] [Continent name not found!]')
        ##-----------State/Region-------##
        print("[~] [State/Region]:", data['regionName'])
        if data['regionName'] == False:
            print('[~] [State/Region not found!]')
        ##----------2-letter Continent Code##---##
        print("[~] [2-letter Continent Code]:", data['continentCode'])
        if data['continentCode'] == False:
            print('[~] [2-letter continent code not found!]')
        ##---Latitude----##
        print("[~] [Latitude]:", data['lat'])
        if data['lat'] == False:
            print('[~] [Latitude not found!]')
        ##----------Longitude------##
        print("[~] [Longitude]:", data['lon'])
        if data['lon'] == False:
            print('[~] [Longitude not found!]')
        ##--------------Timezone---------##
        print("[~] [Timezone]:", data['timezone'])
        if data['timezone'] == False:
            print('[~] [Timezone not found!]')
        ##-------------- ZIP--------------##
        print("[~] [ZIP Code]:", data['zip'])
        if data['zip'] == False:
            print('[~] [ZIP code not found!]')
        ##------------ AS -------------------##
        print("[~] [AS Number and Organization]:", data['as'])
        if data['as'] == False:
            print('[~] [AS number and organization not found!]')
        ##-----------Country Code-----##
        print("[~] [2-letter Country Code]:", data['countryCode'])
        if data['countryCode'] == False:
            print('[~] [2-letter country code not found!]')
        ##-----------Reverse IP---------##
        print("[~] [Reverse DNS for the IP]: ", data['reverse'])
        if data['reverse'] == False:
            print('[~] [Reverse DNS not found!]')
        ##--------------Mobile------##
        print("[~] [Mobile Connection]:", data['mobile'])
        if data['mobile'] == False:
            print('[~] [Mobile connection not found!]')
        ##----Currency----##
        print('[~] [National Currency]:', data['currency'])
        if data['currency'] == False:
            print('[~] [National currency not found!]')
        ##-----District----##
        print('[~] [District (subdivision of city)]:', data['district'])
        if data['district'] == False:
            print('[~] [District not found!]')
        ##-------Proxy-----##
        print('[~] [Proxy, VPN or Tor]:', data['proxy'])
        if data['proxy'] == False:
            print('[~] [VPN not detected.]')
    except KeyError:
        print(f'\n[~] Error retrieving data for {ip}')

def per():
    api2 = f"http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=en"

    time.sleep(1)

    data = requests.get(api2).json()
    ##-----------Query---------##
    print("\n[~] [IP]:", data['query'])
    ##--------------ISP-----------##
    print("[~] [ISP] :", data['isp'])
    if data['isp'] == False:
        print('[~] [ISP not found!]')
    ##------------Org-----------##
    print("[~] [Organization]:", data['org'])
    if data['org'] == False:
        print('[~] [Organization not found!]')
    ##-----------City---------##
    print("[~] [City]:", data['city'])
    if data['city'] == False:
        print('[~] [City not found!]')
    ##-----------Country---------##
    print("[~] [Country Name]:", data['country'])
    if data['country'] == False:
        print('[~] [Country name not found!]')
    ##----------Region-------##
    print("[~] [Region]:", data['region'])
    if data['region'] == False:
        print('[~] [Region not found!]')
    ##---------Continent Name---##
    print("[~] [Continent Name]:", data['continent'])
    if data['continent'] == False:
        print('[~] [Continent name not found!]')
    ##-----------State/Region-------##
    print("[~] [State/Region]:", data['regionName'])
    if data['regionName'] == False:
        print('[~] [State/Region not found!]')
    ##----------2-letter Continent Code##---##
    print("[~] [2-letter Continent Code]:", data['continentCode'])
    if data['continentCode'] == False:
        print('[~] [2-letter continent code not found!]')
    ##---Latitude----##
    print("[~] [Latitude]:", data['lat'])
    if data['lat'] == False:
        print('[~] [Latitude not found!]')
    ##----------Longitude------##
    print("[~] [Longitude]:", data['lon'])
    if data['lon'] == False:
        print('[~] [Longitude not found!]')
    ##--------------Timezone---------##
    print("[~] [Timezone]:", data['timezone'])
    if data['timezone'] == False:
        print('[~] [Timezone not found!]')
    ##-------------- ZIP--------------##
    print("[~] [ZIP Code]:", data['zip'])
    if data['zip'] == False:
        print('[~] [ZIP code not found!]')
    ##------------ AS -------------------##
    print("[~] [AS Number and Organization]:", data['as'])
    if data['as'] == False:
        print('[~] [AS number and organization not found!]')
    ##-----------Country Code-----##
    print("[~] [2-letter Country Code]:", data['countryCode'])
    if data['countryCode'] == False:
        print('[~] [2-letter country code not found!]')
    ##-----------Reverse IP---------##
    print("[~] [Reverse DNS for the IP]: ", data['reverse'])
    if data['reverse'] == False:
        print('[~] [Reverse DNS not found!]')
    ##--------------Mobile------##
    print("[~] [Mobile Connection]:", data['mobile'])
    if data['mobile'] == False:
        print('[~] [Mobile connection not found!]')
    ##----Currency----##
    print('[~] [National Currency]:', data['currency'])
    if data['currency'] == False:
        print('[~] [National currency not found!]')
    ##-----District----##
    print('[~] [District (subdivision of city)]:', data['district'])
    if data['district'] == False:
        print('[~] [District not found!]')
    ##-------Proxy-----##
    print('[~] [Proxy, VPN or Tor]:', data['proxy'])
    if data['proxy'] == False:
        print('[~] [VPN not detected.]')

clear()

if args.track:
    locate(args.track)

if args.trackme:
    per()

if not any(vars(args).values()):
    print("""
    [!] Error: you need to enter an argument.
          
    -track, -t, Enter an IP address to get information.""")