from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
import time


def wwr_scrap(keyword):
    all_job = []
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    #cloudflare 크롤링 우회가 걸려 있음
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)  #playwright를 이용해서 page를 실행시키는데 진짜 브라우저로 보여져야 하기 때문에 browser를 띄움.
    page =browser.new_page()
    page.goto(url, timeout=60000)
    page.wait_for_selector("section.jobs")

    html = page.content()
    browser.close()
                                        
    soup = BeautifulSoup(html, "html.parser")

    jobs = soup.find("div", class_="search-listings__container").find_all("li", class_="new-listing-container")
    for job in jobs:
        if "metana-ad" in job.get("class"): #광고 제거
            jobs.remove(job)
    for job in jobs:
        title = job.find("h3", class_="new-listing__header__title").text
        company_name = job.find("p", class_="new-listing__company-name").text
        location = job.find("p", class_="new-listing__company-headquarters").text
        link = f"https://weworkremotely.com/remote-jobs{job.find('div', class_='tooltip--flag-logo').next_sibling['href']}"
        print(link)
        job_data = {
            "title":title,
            "company_name":company_name,
            "location":location,
            "link":link,
        }
        all_job.append(job_data)
    return all_job

# all_jobs = wwr_scrap("python")

# print(len(all_jobs))

