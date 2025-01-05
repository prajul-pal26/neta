import requests

url = "https://affidavit.eci.gov.in/affidavit-pdf-download/eyJpdiI6IjM3QWxNbXpNb1dRVVB2UHZSdjU3MVE9PSIsInZhbHVlIjoiV2tvNHBLMGxBS3RRVzl2TmdUOU44SzZpMStKdmtEQ0xIc0RKbzBvQlZ3VTQ3K3pQejAvZ094aXByWnMrSEhlZ3RFT20rczJFUGhPWXlmc214OXhLM05YTkhDb3BjYmc1ZGhnZDYyS3Zyazh5QnBFc1k2a0xpd1VzaEFHQzFJSXpock9USGxFd0crRGpLU1pmamlvbmNNTk1PaWNDSm12QjFhQ1hLNVRKUzZNPSIsIm1hYyI6ImUwMDIzNGQzNDI5MGVjMWE2YTBlNmRiNTdlMDQ0MDY5OTVmMDkwOTMzNjZmYTRjY2RkNDM1ZjZkMjM1MDA2ODkiLCJ0YWciOiIifQ=="

payload = {}
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'priority': 'u=0, i',
    'referer': 'https://affidavit.eci.gov.in/show-profile/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Check if the response is successful
if response.status_code == 200:
    with open("affidavit.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)
    print("PDF saved successfully as 'affidavit.pdf'")
else:
    print(f"Failed to fetch the PDF. Status code: {response.status_code}")
