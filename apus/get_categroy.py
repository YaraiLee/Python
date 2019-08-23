#!/usr/bin/env python3
import requests
import json

categroy_url = 'http://test.feed.apusapps.com/mercury/channel/list'
payload = {
	"device": {
		"clientId": "0f242-msn-consumer-4474",
		"mccCode": "",
		"locale": "",
		"newsCountry": "",
		"ip": ""
	},
	"appInfo": {
		"product": "20140001",
		"module": "1"
	}
}

country_list = [
	"US",
	# "KR",
	# "PH",
	# "TH",
	# "ID",
	# "SG",
	# "MY",
	# "HK",
	# "TW",
	# "JP",
	# "BR",
	# "VN",
	# "DK",
	# "DE",
	# "CO",
	# "PE",
	# "CL",
	# "VE",
	# "FR",
	# "GB",
	# "IT",
	# "ES",
	# "RU",
	# "NL",
	# "AU",
	# "NZ",
	# "ZA",
	# "BE",
	# "CA",
	# "CA",
	# "NO",
	# "PT",
	# "TR",
	# "IE",
	# "XL",
	# "AR",
	# "MX",
	# "IN",
]

for country in country_list:
	payload['device']['newsCountry'] = country
	res = requests.post(categroy_url, data=json.dumps(payload))

	res_json = res.json()
	res_code = res_json['code']
	#print(res_code)

	if res_code != 0:
		print("country={}, res_code={}".format(country, res_code))
		continue

	res_data_json = res_json['data']

	res_country = res_data_json['newsCountry']
	print(res_country)

	if res_country != country:
		print("res_country={}, country={}".format(res_country, country))
		continue

	#print("channels=")
	channel_list = res_data_json['channels']
	#print(channel_list)
	# print("countrry={} cates={}".format(country, categroys))

	for channel in channel_list:
		cate_list = channel['cates']
		for cate in cate_list:
			print("id={}, text={}".format(cate['id'], cate['text']))
			#print(cate)


