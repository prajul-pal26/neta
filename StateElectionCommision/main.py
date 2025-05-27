import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data(janpad):
    
    url = "https://sec.up.nic.in/site/WinnerListPRI2021.aspx"
    
    payload = f'__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=W%2FxIDA9gsaw5QxN3%2F7OI0ekWQUqzIH0sa6mWibT95ne4xKslhMaYyfN%2BlYOjVHy6%2BLt%2BhEAUrhhcLjG6P4u80oaFT8uanaFsk93TMrOfLk9hmdiaPGVoTszReXH9AnSVN1PzS9D0BLAZVKDNbObzfmooVGvArIYyafKy8rlU7HeHXbQl3T8kf2S7W%2F1eRJxDp4cu5YA720uqrmP1eYrHAr6OiP0b90OwCTljIn3MU3EGnsGE8zRnzErmcoDmeQD4DBgZIqeSnr8KkkShrD0wOQ7l%2FK%2FV05jVmt8ZbWwOkdXtp%2Bf6D33iUwNEWui%2B3bDTAtpb59Ym%2F1nOS%2BKX80SzFhxqqWkvMBYG2ZKxDpYDJVcXnQHQdtcfSsiCGKmNnEhDJs8Jsmf2itYjjQNk1ONWXLgXvbabw0er%2FXI5VVVtUp5LUxHhU8VJu5r01ovQmbq67nJBd7dF78I5xu82nRaWsXwxvV23Xmac9ZFk%2Bu3Ulpg3Vz8RMCo8tOUfXWY5Zo2YZCedGQHR9PyP%2FknC%2BY8JGGJqPU2uDOrjRI1WQP6SeMRzZMKKINOSD18kAVyGJHOLD2PXBnOigESy5xRmcMCaEO3Iviify7v%2B1sYrtI1wp8YwSVpOS65PMaX6A6X%2FLYPiuls%2F%2BW3QQCwYXmW2g4RqeyeyALVdjuszR5W5Gf9nbRMTcFAKZylaOy22udTfeIGNcdF8dHlSi2dj%2FXeMbPnOmLqRysAgvKEJWKgikW9VjUGVZLXBt6mfMuZIYCYBCW2H2Non79VBIK2wF67xk4DpZei4dgVURdeOmuSONxaejUIf2aRzdt%2Bl35BmSI2DwRss3KOpgBHO1PuNl%2BfI6ksfR%2FYUaf9o%2Brzk8EpW50hGC%2FJ7oST%2B%2BUtkaXhYrLRfmpb2NwtYAQ4MjhrI83dGd2A6nMLwa4H4vJsMBOPVmdngifGrFobhTli%2BsQp%2B%2FNuwuM%2F1kH0obeBVWMogtPtVaxZKL5yLSCbFzkmktXv33iFEg0vu2POds%2Beb77rOqbrVcZI1JcvIkCfPGG4e6mwD3qCnzixAEKtv7t58f8NgXUuQ5yQGzwzY2IL5ihjakecmzcu3Rm3Vun2Gr%2FbctJe9uJM9k7MbyPDNb%2BCvuJ%2FYgoarpQf9aOpUFYcIYyaqHZLdPIeWsWnJ7X9kqg73qQehzHwhP%2BBFwSB2Qn0qju1HreYj%2BY%2BIZwW2QE60N3Si8XTSUXlawEgoV2gN8Q12aJ%2FCcbbYwRFEiCS0EdxgHkyIJ04UJGDCZ2vuxf%2BRrQvE0ZipSJhSoKkeFb%2BUNGXLraz2%2BubeaGtWvCFBgEtO9R%2FoV7yXwfLFSDN3bFDxHUMN6C2YFdQzVa662DBPyz830kBfhbajAW9f4R0Urbgg%2FiVJVJKuVZdwk5mM2h5O%2Fe61evmxgq8DaeAoGhJEiK9WDKw%2BenY37OWYTy7VAIxosMMvsa9MGOn137VJM%2BZiAJPEQBnaVg%2BSyDDQAte79hAl0EFfjFMazJMJaDmpnfSWLn0TYjiCDcRhpx4T8JvATn7WCydT8z10z9O3OIU5o3hPS5SHb1Y4%2FopQQMnBQskCji6tYqED1R57tS8F1kQEpcQ59sLGNopjDsTVe%2BFH%2BAPRFbpw6wWWg9uJCt0X8f4MW1ktmOHtaNdTkUfZvAIRuLU%2Fiq68OnNh9Hk789ajlRTUKwkFGVaz0dSccnY3kE33p6JDhIeSQjYBLffM3xCkzEl5M1tDAU0LPmbdwn68DVuK8oxRCP0P3LF8xyIwIGCzf6ARbSOChVYJtEnOX3CqazJdWcIBml0L%2FHlrAogOR%2FWTjALBc9NKwKlkdoxh9r6wOTU8Ltz7WE32%2BBOtQUEI2oCZF%2FN70Zh%2FW9ltbXvxzIHU2esrTANqfRwEX0x4y6ESrDSiCPnSrhklffiZwojk0dvPXlyFvUuMqmJTYBCf0pOcbvPw7gWxXaOjLrW0EI8CiKYJp9QU272LuYBFnUnDKXEHdepwnLTB5x64USfTG34TD97vkDwD8JtwKqLr0wGBFX8OmQQAWuwpKCGgxVVbd2aZQ3%2FpQ4tsUcbAoy1%2BR89%2FF9GEWefIkEqGZBzfNCRUMnIfeopi2K5zQt1j0B21hmrMtAhgYXpz%2BxeFmM676mChgeFeDjIDzUikX7wA%2FGVcanRpyojec7tUoOtcC1KkDGAWiprHwRq%2FIUAfvaeESh7r8AQnCPL4kaqE%2B4HxBl6cqrdy5GUhWdmU%2B5%2BTwF%2BIj7QMrHf3lhYtqsP3rIqAGdd1Cip3wt4nD%2FwnoYMl0jETEDDjMg69AizAAnaxDvoYu4wjpsJmoXhmq33ofFnCNkWdZPINVDWKtai%2BibOxyKx7P0e6a%2BRSW60EpsOnEBlfkq9ndVusRW8DG5fgupfMRAUROoc3sTLBY42mJIyjGTKaatI2zlP%2BXqDW05wgeyJPeNZlxAGA%2FIWQZPAykrtRiJXdiYcntpOIjrxFL5UJoiSghyq9R1BIrjssHcnpOk0f%2FW37DIxQwHOVWPPC5EvUC3mstlVFjbfJ8qJYFpJ%2FQCouLXeCd54H89LSsuNlHXRQXFujIL7ODbqs%2BLKDgA%3D%3D&__VIEWSTATEGENERATOR=844829E7&__VIEWSTATEENCRYPTED=&ctl00%24ContentPlaceHolder1%24ddlPostTypes=2&ctl00%24ContentPlaceHolder1%24ddlDistrictName={janpad}&ctl00%24ContentPlaceHolder1%24btnSubmit=View%20Details'
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://sec.up.nic.in',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://sec.up.nic.in/site/WinnerListPRI2021.aspx',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'Cookie': 'ASP.NET_SessionId=32qvfstp4wqlnybbl2zjfci3'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find(id='ctl00_ContentPlaceHolder1_GridView1')
    all_tr = soup.find_all('tr')
    column = [i.text for i in all_tr[0].find_all('th')]
    rows=[]
    for row in all_tr[1:]:
        row = [i.text for i in row.find_all('td')]
        rows.append(row)
    df = pd.DataFrame(columns=column, data= rows)
    print(df)    
    df.to_csv(f'{janpad}.csv')


payload = [50, 53, 11, 19, 54, 24, 66, 29, 45, 21, 30, 28, 64, 32, 31, 22, 41, 6, 69, 58, 62, 7, 70, 39, 33, 72, 35, 65, 43, 42, 16, 40, 27, 25, 18, 15, 8, 57, 68, 59, 55, 5, 38, 51, 10, 73, 67, 2, 23, 26, 4, 12, 63, 36, 74, 13, 44, 47, 49, 34, 71, 56, 3, 17, 61, 14, 52, 1, 60, 48, 75, 20, 37, 46, 9]
for i in payload:
    fetch_data(i)