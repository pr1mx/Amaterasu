#coding: utf-8
#!/usr/bin/python3

from xml.etree import ElementTree as etree
from mp3_tagger import MP3File, VERSION_2
from PIL.ExifTags import TAGS, GPSTAGS
from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
from datetime import datetime
from ipwhois import IPWhois
from mutagen.mp3 import MP3
from pprint import pprint
from ftplib import FTP
from PIL import Image
from huepy import *
import dns.resolver
import tldextract
import dns.query
import requests
import dns.zone
import os.path
import zipfile
import shutil
import socket
import pefile
import json
import time
import os
import re

def iploc():
	target = input('Enter domain: ')
	url = 'http://ip-api.com/json/'
	r = requests.get(url + target)
	n = r.text
	jsons = json.loads(n)
	print()
	print(bold(green('IP: ')) + jsons['query'])
	print(bold(green('Status: ')) + jsons['status'])
	print(bold(green('Region: ')) + jsons['regionName'])
	print(bold(green('Country: ')) + jsons['country'])
	print(bold(green('City: ')) + jsons['city'])
	print(bold(green('ISP: ')) + jsons['isp'])
	print(bold(green('Lat,Lon: ')) + str(jsons['lat']) + "," + str(jsons['lon']))
	print(bold(green('ZIPCODE: ')) + jsons['zip'])
	print(bold(green('TimeZone: ')) + jsons['timezone'])
	print(bold(green('AS: ')) + jsons['as'])

def reverse():
	target = input('Enter domain: ')
	url = 'http://api.hackertarget.com/reverseiplookup/?q='
	r = requests.get(url + target)
	n = r.text
	print()
	print(n)

def spider():
	target = input('Enter URL: ')
	if target.startswith('http://'):
		r = requests.get(target)
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)
		for link in links:
			print(bold(purple('Link found: ')) + link)
	elif target.startswith('https://'):
		r = requests.get(target)
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)
		for link in links:
			print(bold(purple('Link found: ')) + link)
	else:
		r = requests.get('http://' + target)
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)
		for link in links:
			print(bold(purple('Link found: ')) + link)

def whois():
	target = input('Enter URL: ')

	try:
		if target == '':
			file = input('Enter file with domains: ')
			filelist = open(file, 'r')

			for domain in filelist.readlines():
				domain = domain.strip()
				addr = socket.gethostbyname(domain)
				obj = IPWhois(addr)
				res = obj.lookup()

				whname = res["nets"][0]['name']
				whdesc = res["nets"][0]['description']
				whemail = res["nets"][0]['abuse_emails']
				whcount = res["nets"][0]['country']
				whstate = res["nets"][0]['state']
				whcidr = res["nets"][0]['cidr']
				whcity = res["nets"][0]['city']
				whadd = res["nets"][0]['address']
				whasncidr = res['asn_cidr']
				whasn = res['asn']
				whasndt = res['asn_date']
				whasnreg = res['asn_registry']

				print()
				if whname == None:
					print(bold(red("NAME ERROR: " )) + "Amaterasu can't find the name.")
				else:
					print(bold(green('Name: ' )) + whname)
				print(bold(green('IP: ')) + addr)
				if whdesc == None:
					print(bold(red("DESCRIPTION ERROR: ")) + "Amaterasu can't find the description.")
				else:
					print(bold(green('Description: ')) + whdesc)
				if whcount == None:
					print(bold(red("Country ERROR: ")) + "Amaterasu can't find the country.")
				else:
					print(bold(green("Country: ")) + whcount)
				if whstate == None:
					print(bold(red("STATE ERROR: ")) + "Amaterasu can't find the state.")
				else:
					print(bold(green('State: ')) + whstate)
				if whcity == None:
					print(bold(red("CITY ERROR: ")) + "Amaterasu can't find the city.")
				else:
					print(bold(green('City: ')) + whcity)
				if whadd == None:
					print(bold(red("ADDRESS ERROR: ")) + "Amaterasu can't find the address.")
				else:
					print(bold(green('Address: ')) + whadd)
				if whemail == None:
					print(bold(red("ABUSE E-MAIL ERROR: " )) + "Amaterasu can't find the abuse e-mail.")
				else:
					print(bold(green('Abuse e-mail: ')) + whemail)
				if whcidr == None:
					print(bold(red("CIDR ERROR: ")) + "Amaterasu can't find the CIDR.")
				else:
					print(bold(green('CIDR: ')) + whcidr)
				if whasncidr == None:
					print(bold(red("ASN CIDR ERROR: ")) + "Amaterasu can't find the ASN_CIDR.")
				else:
					print(bold(green('ASN CIDR: ')) + whasncidr)
				if whasn == None:
					print(bold(red("ASN ERROR: ")) + "Amaterasu can't find the ASN.")
				else:
					print(bold(green('ASN: ')) + whasn)

		if target.startswith('http://'):
			ext = tldextract.extract(target)
			domain = ext.domain
			suffix = ext.suffix

			fullsite = domain + '.' + suffix

			addr = socket.gethostbyname(fullsite)
			obj = IPWhois(addr)
			res = obj.lookup()

			whname = res["nets"][0]['name']
			whdesc = res["nets"][0]['description']
			whemail = res["nets"][0]['abuse_emails']
			whcount = res["nets"][0]['country']
			whstate = res["nets"][0]['state']
			whcidr = res["nets"][0]['cidr']
			whcity = res["nets"][0]['city']
			whadd = res["nets"][0]['address']
			whasncidr = res['asn_cidr']
			whasn = res['asn']
			whasndt = res['asn_date']
			whasnreg = res['asn_registry']

			print()
			if whname == None:
				print(bold(red("NAME ERROR: " )) + "Amaterasu can't find the name.")
			else:
				print(bold(green('Name: ' )) + whname)
			if whdesc == None:
				print(bold(red("DESCRIPTION ERROR: ")) + "Amaterasu can't find the description.")
			else:
				print(bold(green('Description: ')) + whdesc)
			if whcount == None:
				print(bold(red("Country ERROR: ")) + "Amaterasu can't find the country.")
			else:
				print(bold(green("Country: ")) + whcount)
			if whstate == None:
				print(bold(red("STATE ERROR: ")) + "Amaterasu can't find the state.")
			else:
				print(bold(green('State: ')) + whstate)
			if whcity == None:
				print(bold(red("CITY ERROR: ")) + "Amaterasu can't find the city.")
			else:
				print(bold(green('City: ')) + whcity)
			if whadd == None:
				print(bold(red("ADDRESS ERROR: ")) + "Amaterasu can't find the address.")
			else:
				print(bold(green('Address: ')) + whadd)
			if whemail == None:
				print(bold(red("ABUSE E-MAIL ERROR: " )) + "Amaterasu can't find the abuse e-mail.")
			else:
				print(bold(green('Abuse e-mail: ')) + whemail)
			if whcidr == None:
				print(bold(red("CIDR ERROR: ")) + "Amaterasu can't find the CIDR.")
			else:
				print(bold(green('CIDR: ')) + whcidr)
			if whasncidr == None:
				print(bold(red("ASN CIDR ERROR: ")) + "Amaterasu can't find the ASN_CIDR.")
			else:
				print(bold(green('ASN CIDR: ')) + whasncidr)
			if whasn == None:
				print(bold(red("ASN ERROR: ")) + "Amaterasu can't find the ASN.")
			else:
				print(bold(green('ASN: ')) + whasn)

		elif target.startswith('https://'):
			ext = tldextract.extract(target)
			domain = ext.domain
			suffix = ext.suffix

			fullsite = domain + '.' + suffix

			addr = socket.gethostbyname(fullsite)
			obj = IPWhois(addr)
			res = obj.lookup()

			whname = res["nets"][0]['name']
			whdesc = res["nets"][0]['description']
			whemail = res["nets"][0]['abuse_emails']
			whcount = res["nets"][0]['country']
			whstate = res["nets"][0]['state']
			whcidr = res["nets"][0]['cidr']
			whcity = res["nets"][0]['city']
			whadd = res["nets"][0]['address']
			whasncidr = res['asn_cidr']
			whasn = res['asn']
			whasndt = res['asn_date']
			whasnreg = res['asn_registry']

			print()
			if whname == None:
				print(bold(red("NAME ERROR: " )) + "Amaterasu can't find the name.")
			else:
				print(bold(green('Name: ' )) + whname)
			if whdesc == None:
				print(bold(red("DESCRIPTION ERROR: ")) + "Amaterasu can't find the description.")
			else:
				print(bold(green('Description: ')) + whdesc)
			if whcount == None:
				print(bold(red("Country ERROR: ")) + "Amaterasu can't find the country.")
			else:
				print(bold(green("Country: ")) + whcount)
			if whstate == None:
				print(bold(red("STATE ERROR: ")) + "Amaterasu can't find the state.")
			else:
				print(bold(green('State: ')) + whstate)
			if whcity == None:
				print(bold(red("CITY ERROR: ")) + "Amaterasu can't find the city.")
			else:
				print(bold(green('City: ')) + whcity)
			if whadd == None:
				print(bold(red("ADDRESS ERROR: ")) + "Amaterasu can't find the address.")
			else:
				print(bold(green('Address: ')) + whadd)
			if whemail == None:
				print(bold(red("ABUSE E-MAIL ERROR: " )) + "Amaterasu can't find the abuse e-mail.")
			else:
				print(bold(green('Abuse e-mail: ')) + whemail)
			if whcidr == None:
				print(bold(red("CIDR ERROR: ")) + "Amaterasu can't find the CIDR.")
			else:
				print(bold(green('CIDR: ')) + whcidr)
			if whasncidr == None:
				print(bold(red("ASN CIDR ERROR: ")) + "Amaterasu can't find the ASN_CIDR.")
			else:
				print(bold(green('ASN CIDR: ')) + whasncidr)
			if whasn == None:
				print(bold(red("ASN ERROR: ")) + "Amaterasu can't find the ASN.")
			else:
				print(bold(green('ASN: ')) + whasn)
		else:
			addr = socket.gethostbyname(target)
			obj = IPWhois(addr)
			res = obj.lookup()

			whname = res["nets"][0]['name']
			whdesc = res["nets"][0]['description']
			whemail = res["nets"][0]['abuse_emails']
			whcount = res["nets"][0]['country']
			whstate = res["nets"][0]['state']
			whcidr = res["nets"][0]['cidr']
			whcity = res["nets"][0]['city']
			whadd = res["nets"][0]['address']
			whasncidr = res['asn_cidr']
			whasn = res['asn']
			whasndt = res['asn_date']
			whasnreg = res['asn_registry']

			print()
			if whname == None:
				print(bold(red("NAME ERROR: " )) + "Amaterasu can't find the name.")
			else:
				print(bold(green('Name: ' )) + whname)
			if whdesc == None:
				print(bold(red("DESCRIPTION ERROR: ")) + "Amaterasu can't find the description.")
			else:
				print(bold(green('Description: ')) + whdesc)
			if whcount == None:
				print(bold(red("Country ERROR: ")) + "Amaterasu can't find the country.")
			else:
				print(bold(green("Country: ")) + whcount)
			if whstate == None:
				print(bold(red("STATE ERROR: ")) + "Amaterasu can't find the state.")
			else:
				print(bold(green('State: ')) + whstate)
			if whcity == None:
				print(bold(red("CITY ERROR: ")) + "Amaterasu can't find the city.")
			else:
				print(bold(green('City: ')) + whcity)
			if whadd == None:
				print(bold(red("ADDRESS ERROR: ")) + "Amaterasu can't find the address.")
			else:
				print(bold(green('Address: ')) + whadd)
			if whemail == None:
				print(bold(red("ABUSE E-MAIL ERROR: " )) + "Amaterasu can't find the abuse e-mail.")
			else:
				print(bold(green('Abuse e-mail: ')) + whemail)
			if whcidr == None:
				print(bold(red("CIDR ERROR: ")) + "Amaterasu can't find the CIDR.")
			else:
				print(bold(green('CIDR: ')) + whcidr)
			if whasncidr == None:
				print(bold(red("ASN CIDR ERROR: ")) + "Amaterasu can't find the ASN_CIDR.")
			else:
				print(bold(green('ASN CIDR: ')) + whasncidr)
			if whasn == None:
				print(bold(red("ASN ERROR: ")) + "Amaterasu can't find the ASN.")
			else:
				print(bold(green('ASN: ')) + whasn)
	except Exception:
		pass

def email_ex():
	target = input('Enter URL: ')

	ext = tldextract.extract(target)
	domain = ext.domain
	suffix = ext.suffix
	fullsite = domain + '.' + suffix

	hunter_api = '' #ENTER YOUR API HERE.
	hunter_web = 'https://api.hunter.io/v2/domain-search?domain={}&api_key={}'.format(fullsite, hunter_api)

	all_mails = []

	print()
	if target.startswith('https://'):
		emails_searcher = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')
		r = requests.get(target)
		emails = emails_searcher.findall(r.text)
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)

		for address in emails:
			all_mails.append(address)
			#print(bold(green('E-mail found: ')) + address)
		try:
			r2 = requests.get(hunter_web)
			emails1 = emails_searcher.findall(r2.text)
			links2 = link_find.findall(r2.text)
			for a in emails1:
				all_mails.append(a)
				#print(bold(green('E-mail found: ')) + a)
		except Exception as e:
			pass

		for link in links:
			#print(bold(purple('Link found: ')) + link)
			r1 = requests.get('https://' + fullsite + link)
			new_mails = emails_searcher.findall(r1.text)

			for email in new_mails:
				all_mails.append(email)
				#print(bold(green('E-mail found: ')) + email)
			#print()

			print(bold(green('Google dorking: ')))
			try:
				for url in search('site:'+ fullsite + ' -google.com +@(hotmail|yahoo|bol|gmail|' + domain + '|mail) ext:txt'):
					print(url)
			except Exception as e:
				print(bad('Google dorking failed: {}'.format(e)))
				pass


	elif target.startswith('http://'):
		emails_searcher = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')
		r = requests.get(target)
		emails = emails_searcher.findall(r.text)
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)

		for address in emails:
			all_mails.append(emails)
			#print(bold(green('E-mail found: ')) + address)
		try:
			r2 = requests.get(hunter_web)
			emails1 = emails_searcher.findall(r2.text)
			links2 = link_find.findall(r2.text)
			for a in emails1:
				all_mails.append(a)
				#print(bold(green('E-mail found: ')) + a)
		except Exception as e:
			pass

		for link in links:
			#print(bold(purple('Link found: ')) + link)
			r1 = requests.get('https://' + fullsite + link)
			new_mails = emails_searcher.findall(r1.text)

			for email in new_mails:
				all_mails.append(email)
				#print(bold(green('E-mail found: ')) + email)
			#print()

			print(bold(green('Google dorking: ')))
			try:
				for url in search('site:'+ fullsite + ' -google.com +@(hotmail|yahoo|bol|gmail|' + domain + '|mail) ext:txt'):
					print(url)
			except Exception as e:
				print(bad('Google dorking failed: {}'.format(e)))
				pass
	else:
		emails_searcher = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')
		newT = 'http://' + target
		r = requests.get(newT)
		r2 = requests.get(hunter_web)

		emails = emails_searcher.findall(r.text)
		emails1 = emails_searcher.findall(r2.text)
		
		link_find = re.compile('href="(.*?)"')
		links = link_find.findall(r.text)
		links2 = link_find.findall(r2.text)

		for address in emails:
			all_mails.append(emails)
			#print(bold(green('E-mail found: ')) + address)
		for a in emails1:
			all_mails.append(a)
			#print(bold(green('E-mail found: ')) + a)

		for link in links:
			#print(bold(purple('Link found: ')) + link)
			r1 = requests.get('https://' + fullsite + link)
			new_mails = emails_searcher.findall(r1.text)

			for email in new_mails:
				all_mails.append(email)
				#print(bold(green('E-mail found: ')) + email)
			print()
			print(bold(green('Google dorking: ')))
			try:
				for url in search('site:'+ fullsite + ' -google.com +@(hotmail|yahoo|bol|gmail|' + domain + '|mail) ext:txt'):
					print(url)
			except Exception as e:
				print(bad('Google dorking failed: {}'.format(e)))
				pass

	if all_mails != None:
		print(bold(green('All e-mails:')))
		print('\n'.join(all_mails))
		print('\nE-mails extracted: ' + str(len(all_mails)))
	else:
		print('0 e-mails extracted.')
	
def subdomain():
	target = input('Enter domain: ')
	if target.startswith('http://'):
		subdomains = []

		r = requests.get('https://crt.sh/?q=%.{}&output=json'.format(target))

		if r.status_code != 200:
			print(bad('crt.sh not available.'))
			pass

		js = json.loads('[{}]'.format(r.text.replace('}{', '},{')))

		for (key, value) in enumerate(js):
			subdomains.append(value['name_value'])

		subdomains = sorted(set(subdomains))

		for subdomain in subdomains:
			print(good('Subdomain found: ' + subdomain))

	elif target.startswith('https://'):
		subdomains = []

		r = requests.get('https://crt.sh/?q=%.{}&output=json'.format(target))

		if r.status_code != 200:
			print(bad('crt.sh not available.'))
			pass

		js = json.loads('[{}]'.format(r.text.replace('}{', '},{')))

		for (key, value) in enumerate(js):
			subdomains.append(value['name_value'])

		subdomains = sorted(set(subdomains))

		for subdomain in subdomains:
			print(good('Subdomain found: ' + subdomain))

	else:
		subdomains = []

		r = requests.get('https://crt.sh/?q=%.{}&output=json'.format(target))

		if r.status_code != 200:
			print(bad('crt.sh not available.'))
			pass

		js = json.loads('[{}]'.format(r.text.replace('}{', '},{')))

		for (key, value) in enumerate(js):
			subdomains.append(value['name_value'])

		subdomains = sorted(set(subdomains))

		for subdomain in subdomains:
			print(good('Subdomain found: ' + subdomain))

def dns_ex():
	target = input('Enter URL: ')
	dnsr = dns.resolver

	if target.startswith('https://'):
		ext = tldextract.extract(target)
		domain = ext.domain
		suffix = ext.suffix

		target = domain + '.' + suffix

		try:
			print()
			ns = dnsr.query(target, 'NS')
			for rs in ns:
				print(bold(green('NS records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > NS records.'))

		try:
			print()
			a = dnsr.query(target, 'A')
			for rs in a:
				print(bold(green('A records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > A records.'))

		try:
			print()
			mx = dnsr.query(target, 'MX')
			for rs in mx:
				print(bold(green('MX records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > MX records.'))

		try:
			print()
			txt = dnsr.query(target, 'TXT')
			for spf in txt:
				print(bold(green('SPF records: ')) + str(spf))
		except dns.exception.DNSException:
			print(bad('Query failed > SPF records.'))

	elif target.startswith('http://'):
		ext = tldextract.extract(target)
		domain = ext.domain
		suffix = ext.suffix

		target = domain + '.' + suffix

		try:
			print()
			ns = dnsr.query(target, 'NS')
			for rs in ns:
				print(bold(green('NS records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > NS records.'))

		try:
			print()
			a = dnsr.query(target, 'A')
			for rs in a:
				print(bold(green('A records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > A records.'))

		try:
			print()
			mx = dnsr.query(target, 'MX')
			for rs in mx:
				print(bold(green('MX records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > MX records.'))

		try:
			print()
			txt = dnsr.query(target, 'TXT')
			for spf in txt:
				print(bold(green('SPF records: ')) + str(spf))
		except dns.exception.DNSException:
			print(bad('Query failed > SPF records.'))

	else:
		ext = tldextract.extract(target)
		domain = ext.domain
		suffix = ext.suffix

		target = domain + '.' + suffix

		try:
			print()
			ns = dnsr.query(target, 'NS')
			for rs in ns:
				print(bold(green('NS records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > NS records.'))

		try:
			print()
			a = dnsr.query(target, 'A')
			for rs in a:
				print(bold(green('A records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > A records.'))

		try:
			print()
			mx = dnsr.query(target, 'MX')
			for rs in mx:
				print(bold(green('MX records: ')) + str(rs))
		except dns.exception.DNSException:
			print(bad('Query failed > MX records.'))

		try:
			print()
			txt = dnsr.query(target, 'TXT')
			for spf in txt:
				print(bold(green('SPF records: ')) + str(spf))
		except dns.exception.DNSException:
			print(bad('Query failed > SPF records.'))

def ftp_brute():
	target = input('Enter IP or domain: ')
	username = input('Enter USERNAME wordlist: ')
	password = input('Enter PASSWORD wordlist: ')

	ftp = FTP(target)
	print()
	answers = {'230 Anonymous access granted, restrictions apply', '230 Login successfull.', 'Guest login ok, access restrictions apply.', 'User anonymous logged in.'}

	try:
		if ftp.login() in answers:
			print(good('Anonymous login is open.'))
			print(good('Username: anonymous'))
			print(good('Password: anonymous@'))
			ftp.close()
		else:
			ftp.close()
	except:
		ftp.close()
		pass

	try:
		usernames = open(username)
		passwords = open(password)

		answers = {'230 Anonymous access granted, restrictions apply', '230 Login successfull.', 'Guest login ok, access restrictions apply.', 'User anonymous logged in.'}
		
		for user in usernames.readlines():
			for passw in passwords.readlines():
				user = user.strip()
				passw = passw.strip()
				ftp = FTP(target)

				try:
					if ftp.login(user, passw) in answers:
						print()
						print(good('Success.'))
						print(good('Username: ' + user))
						print(good('Password: ' + passw))
						ftp.close()
						#break
					else:
						print()
						print(bad('Failed.'))
						print(bad('Username failed: ' + user))
						print(bad('Password failed: ' + passw))
						ftp.close()
				except Exception as e:
					print()
					print(bad('Failed: {}'.format(e)))
					print(bad('Username failed: ' + user))
					print(bad('Password failed: ' + passw))
					ftp.close()
	except Exception as e:
		print(bad('Bruteforce failed: ' + e))
		ftp.quit()
		
def metadata():
	print('Only .MP3, .JPG, .JPEG, .PNG, .DOCX and .PDF.')

	try:
		file = input(que('Enter file location: '))
		
		if file.endswith('.jpg'):
			print()
			try:
				for (tag, value) in Image.open(file)._getexif().items():
					print('%s = %s' % (TAGS.get(tag), value))
			except Exception as e:
				print('Could not get any information.')

		if file.endswith('.jpeg'):
			print()
			try:
				for (tag, value) in Image.open(file)._getexif().items():
					print('%s = %s' % (TAGS.get(tag), value))
			except Exception as e:
				print('Could not get any information.')

		if file.endswith('.png'):
			print()
			try:
				for (tag, value) in Image.open(file)._getexif().items():
					print('%s = %s' % (TAGS.get(tag), value))
			except Exception as e:
				print('Could not get any information.')

		elif file.endswith('.pdf'):
			print()
			stat = os.stat(file)
			try:
				if 'Linux' in platform.system() or 'darwin' in platform.system():
					print(bold(green('Change time: ')) + stat.st_ctime)
				elif 'Windows' in platform.system():
					print(bold(green('Creation date: ')) + time.ctime(os.path.getctime(file)))
				else:
					print(bad('Cant extract creation date. Platform {} is unsupported.'.format(platform.system())))
				print(bold(green('Access time: ')) + time.ctime(os.path.getatime(file)))
				print(bold(green('Modified time: ')) + time.ctime(os.path.getmtime(file)))
				with open(file, 'rb') as f:
					pdf = PdfFileReader(f)
					info = pdf.getDocumentInfo()
					number = pdf.getNumPages()

					try:
						author = info.author
						print(bold(green('Author: ')) + str(author))
					except Exception:
						pass
					try:
						creator = info.creator
						print(bold(green('Creator: ')) + str(creator))
					except Exception:
						pass
					try:
						producer = info.producer
						print(bold(green('Producer: ')) + str(producer))
					except Exception:
						pass
					try:
						subject = info.subject
						print(bold(green('Subject: ')) + str(subject))
					except Exception:
						pass
					try:
						title = info.title
						print(bold(green('Title: ')) + str(title))
					except Exception:
						pass
					
					print(bold(green('Number of pages: ')) + str(number))
					print(bold(green('File size: ')) + str(stat.st_size))
					print(bold(green('File mode: ')) + str(stat.st_mode))
					print(bold(green('File inode: ')) + str(stat.st_ino))
					print(bold(green('Group ID: ')) + str(stat.st_gid))
					print(bold(green('Owner USER ID: ')) + str(stat.st_uid))
			except Exception as e:
				print(e)

		elif file.endswith('.mp3'):
			print()
			try:
				mp3 = MP3File(file)
				tags = mp3.get_tags()
				
				mp3.set_version(VERSION_2)

				title = mp3.song
				artist = mp3.artist
				alb = mp3.album
				trac = mp3.track
				genr = mp3.genre
				year = mp3.year
				band = mp3.band
				composer = mp3.composer
				copyright = mp3.copyright
				publisher = mp3.publisher
				url = mp3.url
				comment = mp3.comment

				audio = MP3(file)
				length = audio.info.length
				bitrate = audio.info.bitrate
				channels = audio.info.channels

				print(bold(green('Title: ')) + str(title))
				print(bold(green('Artist: ')) + str(artist))
				print(bold(green('Band: ')) + str(band))
				print(bold(green('Composer: ')) + str(composer))
				print(bold(green('Publisher: ')) + str(publisher))
				print(bold(green('URL: ')) + str(url))
				print(bold(green('Copyright: ')) + str(copyright))
				print(bold(green('Album: ')) + str(alb))
				print(bold(green('Track: ')) + str(trac))
				print(bold(green('Genre: ')) + str(genr))
				print(bold(green('Year: ')) + str(year))
				print(bold(green('Comment: ')) + str(comment))
				print(bold(green('Bitrate: ')) + str(bitrate))
				print(bold(green('Length: ')) + str(length))
				print(bold(green('Channels: ')) + str(channels))
			except Exception as e:
				print(e)

		elif file.endswith('.docx'):
			print()
			zipfile.is_zipfile(file)
			zfile = zipfile.ZipFile(file)

			#extract key elements for processing
			core_xml = etree.fromstring(zfile.read('docProps/core.xml'))
			app_xml = etree.fromstring(zfile.read('docProps/app.xml'))

			core_map = {
			'title' : 'Title',
			'subject' : 'Subject',
			'creator' : 'Author(s)',
			'keywords' : 'Keywords',
			'description' : 'Description',
			'lastModifiedBy' : 'Last Modified By',
			'modified' : 'Modified Date',
			'created' : 'Created Date', 
			'category' : 'Category',
			'contentStatus' : 'Status',
			'revision' : 'Revision'
			}

			for element in core_xml.getchildren():
				for key, title in core_map.items():
					if key in element.tag:
						if 'date' in title.lower():
							try:
								text = dt.strptime(element.text, '%Y-%m-%dT%H:%M:%SZ')
							except Exception as e:
								pass
						else:
							text = element.text
						print(bold(green('{}: '.format(title))) + '{}'.format(text))

			app_map = {
			'TotalTime' : 'Edit Time (minutes)',
			'Pages' : 'Page Count',
			'Words' : 'Word Count',
			'Characters' : 'Character Count',
			'Lines' : 'Line Count',
			'Paragraphs' : 'Paragraph Count',
			'Company' : 'Company',
			'HyperlinkBase' : 'Hyperlink Base',
			'Slides' : 'Slide count',
			'Notes' : 'Note count',
			'HiddenSlides' : 'Hidden Slide Count'
			}

			for element in app_xml.getchildren():
				for key, title in app_map.items():
					if 'date' in title.lower():
						try:
							text = dt.strptime(element.text, '%Y-%m-%dT%H:%M:%SZ')
						except Exception as e:
							pass
					else:
						text = element.text
					print(bold(green('{}: '.format(title))) + '{}'.format(text))

		elif file.endswith('.exe'):
			stat = os.stat(file)

			link = pefile.PE(file)
			stat = os.stat(file)
			#print(print_info(encoding='utf-8'))
			imp = link.get_imphash()
			errors = link.get_warnings()
			relocs = link.has_relocs()
			checksum = link.verify_checksum()
			strings = link.get_resources_strings()
			print()
			print(bold(green('Hash of Import Address Table (IAT): ')) + imp)
			print(bold(green('Errors: ')) + str(errors))
			print(bold(green('Has relocation directory: ')) + str(relocs))
			print(bold(green('Checksum: ')) + str(checksum))
			print(bold(green('File size: ')) + str(stat.st_size))
			print()
			print(bold(red('Strings')))
			for string in strings:
				print(bold(green('String: ')) + string)
			print()
			print(bold(red('Directory Entry Import')))
			for entry in link.DIRECTORY_ENTRY_IMPORT:
				print('\t' + entry.dll.decode('utf-8'))

	except KeyboardInterrupt:
		print()
		#print('Soon.')
		#target = input(strike(que('Enter target: ')))