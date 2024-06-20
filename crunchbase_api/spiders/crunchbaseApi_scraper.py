import scrapy
import json
from string import ascii_lowercase, digits

class CrunchbaseApiSpider(scrapy.Spider):
	name = 'companies'
	
	custom_settings = {
		'ITEM_PIPELINES': {
			'crunchbase_api.pipelines.CrunchbaseApiPipeline': 300,
			}
		}

	def start_requests(self):
		chars = ascii_lowercase + digits
		print(chars)
		for i in chars:
			for j in chars:
				for k in chars:
					query = f'{i}{j}'
					url = f'https://www.crunchbase.com/v4/data/autocompletes?query={query}&collection_ids=organizations&limit=25&source=topSearch'
					yield scrapy.Request(url, dont_filter=True, callback=self.parse)
					

	def parse(self, response):
		data = json.loads(response.body)

		for entity in data['entities']:
			uuid = entity['identifier'].get('uuid')
			name = entity['identifier'].get('value')
			image_id = entity['identifier'].get('image_id')
			permalink = entity['identifier'].get('permalink')
			url =f"https://www.crunchbase.com/v4/data/entities/organizations/{permalink}?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22is_locked%22%5D&layout_mode=view_v2"
			headers = {
				'accept': 'application/json, text/plain, */*',
				'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
				'dnt': '1',
				'if-none-match': 'W/"1718373516445"',
				'priority': 'u=1, i',
				'referer': f'https://www.crunchbase.com/organization/{permalink}',
				'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"macOS"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
				'x-cb-client-app-instance-id': 'b93920f3-7adb-4248-8a60-5bfaa5496cec',
				'x-requested-with': 'XMLHttpRequest',
				# 'Cookie': 'cid=CigiGGZtNHYAqAAbMJTJAg==; __cflb=02DiuJLCopmWEhtqNz6NSRa7oaPd5PpY2R2KEHHgSax6G; _pxhd=f6bqKLzwsovGyAdeIGIq4WMdb/3YOZwU8uNrGHkTo/HdBHLIf821BdmF66pIu6nRxWJIHt9Gtoe9V0SUT2Vy7w; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI5MDcyZDNjZi0wOGJlLTRlNGItYjg0NS05ODgyMWNlYzZiZTciLCJpc3MiOiJ1c2Vyc2VydmljZV8zZGYzY2E2OV83MjYiLCJzdWIiOiJhMGJiOTIxNy1mMTQ0LTQzZjMtYTI4Yi0xZDIyMjk2NzlkNDQiLCJleHAiOjE3MTg0MzMxODYsImlhdCI6MTcxODQzMjg4NiwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTRuUjNoQ01tN0wvczVwaGdQekpFZDdCSEFBVjhORzQ5VDh1N0w4Z0xEd1ZWcVdSUFRaOEVyUXpybmxlSUdPOTB2QlY4RVB4YVBkUjRhSHJCeGM4NEpzWnpoQkZ5MGpoUDRMMlFHVEhqVWRWRWZDKzZQZndmdVlLVythMEJpR3ppcXVNdWJYejB1TjF2aHhYNU16a2RuQzQzTnI5UlhXeHZ4VXJwczJaSllVbmJlRnBGU2NYNUwyWEdPNlJSZ2hTRm1rSm1nL0x2MkxRWmEwUEdFTVV1bXhFQTlaK3Fta2tHL0JqWTU4elF6ZXFmNmJiU3RtdnlERlNyRFo4VGNhTDF4QlRpOGxMMDk5bkVMRStxOUFYMnlneXZaeVhwZE9TcVpVZllVSElIN1lpMzdiOTBqMUFhN05IbFUvdE1mSlFrUT09IiwicHVibGljIjp7InNlc3Npb25faGFzaCI6Ii0yMTMxMDgzNzQzIn19.08ujWNSxhOk3upHXqsm1voWXG7hFAy0nJvxcdxPLTWK_EfBxCKzLwP1VAHHW2XDdCfxhas9ZxywLgfwEYOXhtg; cb_analytics_consent=granted'
			}

			yield scrapy.Request(url=url,headers=headers,callback=self.company_detail)
   
	def company_detail(self,response):
		data = json.loads(response.text)
		property = data["properties"]
		title = property["title"]
		# short_description = property["short_description"]
		# global_rank = data['cards']["semrush_summary"]["semrush_global_rank"]
		# visits_latest_month = data['cards']["semrush_summary"]["semrush_visits_latest_month"]

		yield{
			'title':title,
			# 'short_description':short_description,
			# 'global_rank':global_rank,
			# 'visits_latest_month':visits_latest_month,
		}	
  

  