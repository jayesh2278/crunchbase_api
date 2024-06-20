import requests
import json
import re

def remove_leading_zeros(input_string):
    if input_string is None:
        return None
    # Remove leading zeros from numbers after underscores
    modified_string = re.sub(r'_0*(\d+)', r'_\1', input_string)
    # Remove the initial part before the first underscore (assuming it's a single character followed by an underscore)
    modified_string = re.sub(r'^[^_]*_', '', modified_string)
    return modified_string



url = "https://www.crunchbase.com/v4/data/entities/organizations/apple?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22is_locked%22%5D&layout_mode=view_v2"

payload = {}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
    'dnt': '1',
    'if-none-match': 'W/"1718373516445"',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-cb-client-app-instance-id': 'b93920f3-7adb-4248-8a60-5bfaa5496cec',
    'x-requested-with': 'XMLHttpRequest',
    'Cookie': 'cid=CigiGGZtNHYAqAAbMJTJAg==; __cflb=02DiuJLCopmWEhtqNz6NSRa7oaPd5PpY2R2KEHHgSax6G; _pxhd=Gop16yW0Se1ixNqV/NQeGPR7mpwbGCzaCdsl6xcYwqcTriXdowCSrwdxWfdZEEgyyqM/vtD6EiX-9vUdcb6KmQ; authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI5MDcyZDNjZi0wOGJlLTRlNGItYjg0NS05ODgyMWNlYzZiZTciLCJpc3MiOiJ1c2Vyc2VydmljZV8zZGYzY2E2OV83MjYiLCJzdWIiOiJhMGJiOTIxNy1mMTQ0LTQzZjMtYTI4Yi0xZDIyMjk2NzlkNDQiLCJleHAiOjE3MTg0NDA4NTUsImlhdCI6MTcxODQ0MDU1NSwicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTRuUjNoQ01tN0wvczVwaGdQekpFZDdCSEFBVjhORzQ5VDh1N0w4Z0xEd1ZWcVdSUFRaOEVyUXpybmxlSUdPOTB2QlY4RVB4YVBkUjRhSHJCeGM4NEpzWnpoQkZ5MGpoUDRMMlFHVEhqVWRWRWZDKzZQZndmdVlLVythMEJpR3ppcXVNdWJYejB1TjF2aHhYNU16a2RuQzQzTnI5UlhXeHZ4VXJwczJaSllVbmJlRnBGU2NYNUwyWEdPNlJSZ2hTRm1rSm1nL0x2MkxRWmEwUEdFTVV1bXhFQTlaK3Fta2tHL0JqWTU4elF6ZXFmNmJiU3RtdnlERlNyRFo4VGNhTDF4QlRpOGxMMDk5bkVMRStxOUFYMnlneXZaeVhwZE9TcVpVZllVSElIN1lpMzdiOTBqMUFhN05IbFUvdE1mSlFrUT09IiwicHVibGljIjp7InNlc3Npb25faGFzaCI6Ii0yMTMxMDgzNzQzIn19.Cjz4WTchltklVw_0y8ifss9sih-gH7p6-tJhjx0YUi45ou8cPpB_jX1QcLlD3Ww9lvO_lIHshe8-KNa7lSoiaQ; cb_analytics_consent=granted'
}

response = requests.get(url, headers=headers, data=payload)
data = json.loads(response.text)



# Extracting and printing data
property = data["properties"]
title = property["title"]
short_description = property["short_description"]

visits_latest_month = data['cards']["semrush_summary"].get("semrush_visits_latest_month")

similar_organization_count = data['cards']["company_overview_highlights"].get("num_org_similarities")
num_current_positions = data['cards']["company_overview_highlights"].get("num_current_positions")
num_investors = data['cards']["company_overview_highlights"].get("num_investors")
num_contacts = data['cards']["company_overview_highlights"].get("num_contacts")
num_acquisitions = data['cards']["company_overview_highlights"].get("num_acquisitions")
funding_total_amount = data['cards']["company_overview_highlights"].get("funding_total")
if funding_total_amount:
    funding_total_amount = funding_total_amount.get("value")
    

company_type = data['cards']["overview_company_fields"]["company_type"]

contact_field_email = data['cards']["contact_fields"].get("contact_email")
social_field = data['cards']["social_fields"]
if social_field:
    linkedin = social_field.get("linkedin")['value']
    twitter = social_field.get("twitter")['value']
else:
    linkedin = None
    twitter = None
company_about_fields2 = data['cards']["company_about_fields2"]
website = company_about_fields2["website"]["value"]
ipo_status = company_about_fields2["ipo_status"]
num_employees_enum = remove_leading_zeros(company_about_fields2.get("num_employees_enum"))
last_funding_type = company_about_fields2.get("last_funding_type")
location_list = [location["permalink"] for location in company_about_fields2["location_identifiers"]]
rank_org_company = company_about_fields2["rank_org_company"]

overview_fields_extended = data['cards']["overview_fields_extended"]
headquarters_regions = overview_fields_extended["location_group_identifiers"][0]["value"]
founded_on = overview_fields_extended["founded_on"]["value"]
founder = overview_fields_extended.get("founder_identifiers")
if founder:
    founder = founder[0].get("value")


operating_status = overview_fields_extended["operating_status"]
hub_tags = overview_fields_extended.get("hub_tags")
if hub_tags:
    hub_tags = (',').join(hub_tags)

categories_list = [category["permalink"] for category in overview_fields_extended["categories"]]
legal_name = overview_fields_extended.get("legal_name")

# Printing all extracted data
print(f"Title: {title}")
print(f"Short Description: {short_description}")
print(f"Visits Latest Month: {visits_latest_month}")
print(f"Similar Organization Count: {similar_organization_count}")
print(f"Number of Current Positions: {num_current_positions}")
print(f"Number of Investors: {num_investors}")
print(f"Number of Contacts: {num_contacts}")
print(f"Number of Acquisitions: {num_acquisitions}")
print(f"Funding Total Amount: {funding_total_amount}")
print(f"Company Type: {company_type}")
print(f"Contact Email: {contact_field_email}")
print(f"LinkedIn: {linkedin}")
print(f"Twitter: {twitter}")
print(f"Website: {website}")
print(f"IPO Status: {ipo_status}")
print(f"Number of Employees Enum: {num_employees_enum}")
print(f"Last Funding Type: {last_funding_type}")
print(f"Locations: {', '.join(location_list)}")
print(f"Rank Org Company: {rank_org_company}")
print(f"Headquarters Regions: {headquarters_regions}")
print(f"Founded On: {founded_on}")
print(f"Founder: {founder}")
print(f"Operating Status: {operating_status}")
print(f"Hub Tags: {hub_tags}")
print(f"Categories: {', '.join(categories_list)}")
print(f"Legal Name: {legal_name}")
