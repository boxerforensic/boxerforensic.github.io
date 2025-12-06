import csv

def save_to_file(keyword, all_jobs): 
    file = open(f"{keyword}.csv", "w", encoding="UTF-8") #키워드를 가지고 와서 이름을 만들고
    writer = csv.writer(file)
    writer.writerow(all_jobs[0].keys()) #all_jobs의 첫번째 항목의 키들을 가지고 와서 csv에 첫줄을 완성한다.
    for job in all_jobs:
        writer.writerow(job.values())
    file.close()