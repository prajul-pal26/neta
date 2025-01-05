import requests
from bs4 import BeautifulSoup
import os

class ECI:
    def __init__(self):
        self.result = []
        self.fetch_session =requests.Session()
        self.token = None
        self.pdfkey =[]
        self.headers =  {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }
        
    def fetch_token(self):
        url = 'https://affidavit.eci.gov.in'
        response = self.fetch_session.get(url = url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find('input')['value']
        self.token = soup
        
    def fetch_main_list(self):
        url = "https://affidavit.eci.gov.in/CandidateCustomFilter"
        payload = f'_token={self.token}&electionType={self.time_period}&election={self.type}&states={self.state}&phase={self.phase}&constId={self.constituency}&submitName=&search='
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://affidavit.eci.gov.in',
        'priority': 'u=0, i',
        'referer': 'https://affidavit.eci.gov.in/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        response = self.fetch_session.post(url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find('table',id='data-tab')
        soup = [i['href'] for i in soup.find_all('a')[::2]]
        self.result +=soup
        
    def fetch_next_data(self):
        flag = True
        page =2
        
        while(flag is True):
            url = f"https://affidavit.eci.gov.in/CandidateCustomFilter?_token={self.token}&electionType=27-AC-GENERAL-3-51&election=27-AC-GENERAL-3-51&states=S13&phase=3&constId=42&page={page}"
            payload = {}
            response =self.fetch_session.get( url, headers=self.headers, data=payload)
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find('table',id='data-tab')
            soup = [i['href'] for i in soup.find_all('a')[::2]]
            if len(soup)==0:
                flag = False
                break
            self.result +=soup
            page+=1
            
    def parse_data(self):
        for link in self.result:
            url = link
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://affidavit.eci.gov.in/CandidateCustomFilter?_token=8tuW59yen0R12EV2j1ut2TO52JYhbqJDo0ksxqmG&electionType=27-AC-GENERAL-3-51&election=27-AC-GENERAL-3-51&states=S13&phase=3&constId=42&page=2',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            response = requests.get( url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            button = soup.find('button', {'onclick': True})
            candidate_id = None
            if button:
                # Extract the candidate ID from the onclick attribute
                onclick_attr = button['onclick']
                if "increaseDownloadCount" in onclick_attr:
                    candidate_id = onclick_attr.split("(")[1].split(")")[0]
            content= [i.text.strip() for i in soup.find_all('p')]
            data = {
                'name':content[3],
                'assembly': content[7], 
                'state': content[9], 
                'candidate_id': candidate_id,
                'pdf_url':soup.find('input',id=f'pdfUrl{candidate_id}')['value']
            }
            self.parse_file(**data )
            
    def parse_file(self, name, assembly, state, pdf_url, candidate_id):
        
        url = f"https://affidavit.eci.gov.in/affidavit-pdf-download/{pdf_url}"

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
        pdf_name = ''.join(['_' if i==" " else i for i in name+' '+assembly+' '+state])
        # Check if the response is successful
        
        download_folder = "downloads"
        os.makedirs(download_folder, exist_ok=True)
        
        if response.status_code == 200:
            file_path = os.path.join(download_folder, f"{pdf_name}.pdf")
            with open(file_path, "wb") as pdf_file:
                pdf_file.write(response.content)
            print("PDF saved successfully as 'affidavit.pdf'")
        else:
            print(f"Failed to fetch the PDF. Status code: {response.status_code}")


    def fetch_data(self, data):
        self.time_period= data['time_period']
        self.type = data['type']
        self.state= data['state']
        self.phase=data['phase']
        self.constituency= data['constituency']
        
        self.fetch_token()
        self.fetch_main_list()
        self.fetch_next_data()
        self.parse_data()


if __name__ == "__main__": 
    obj = ECI()
    data ={
        'time_period':"27-AC-GENERAL-3-51",
        'type':"27-AC-GENERAL-3-51",
        'state':'S13',
        'phase':'3',
        'constituency': '42',
    }
    obj.fetch_data(data)
 
