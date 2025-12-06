from bs4 import BeautifulSoup
import requests

 
def web3_scrap(keyword):
    all_jobs = [] #통합 일자리 저장
    page =0 
    while True:
        page += 1
        url = f"https://web3.career/{keyword}-jobs?page={page}"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("tbody", class_="tbody").find_all("tr") #일자리 태그인 tr태그를 탐색

        for job in jobs:
            id = job.get("id") #광고를 제거
            if id == "sponsor_2":
                jobs.remove(job)
        #일자리를 파싱
        for job in jobs:
            title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text
            link = f"https://web3.career{job.find("a")["href"]}"
            company_name = job.find("td", class_="job-location-mobile").find("h3").text
            location = job.find("td", class_="job-location-mobile").find_next_sibling(class_="job-location-mobile").text
            job_data = {
            "title":title,
            "company_name":company_name,
            "location":location,
            "link":link,
            }
            all_jobs.append(job_data)
            #페이지 확인 로직 번호클래스의 disabled를 확인해서 계속 돌릴지 말지 확인
        border = soup.find("ul", class_="pagination").find_all("li")[-1]
        if "disabled" in border.get("class"): # 번호클라스 안에 disabled가 있으면 break
            break 
    return all_jobs

# all_jobs = web3_scrap("python")                
# print(len(all_jobs))