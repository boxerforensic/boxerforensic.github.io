from bs4 import BeautifulSoup
import requests



def berlinen_Scrap(keyword):
    all_jobs = []
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"
    print(f"https://berlinstartupjobs.com/skill-areas/{keyword} 페이지를 탐색합니다.\n")
    custom_headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=custom_headers)
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
    for job in jobs:
        title = job.find("h4", class_="bjs-jlid__h").find("a").text
        link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        company_name = job.find("a", class_="bjs-jlid__b").text
        location = job.find("div", class_="bjs-jlid__description").text
        job_data = {
            "title":title,
            "company_name":company_name,
            "location":location,
            "link":link,
        }
        all_jobs.append(job_data)
    
    return all_jobs

# all_job = berlinen_Scrap("python")
# print(len(all_job))