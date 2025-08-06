import requests
from datetime import datetime

TYPE = "year"
NUMBER = "random"
URL = f"http://numbersapi.com/{NUMBER}/{TYPE}"

# README 파일 경로
README_PATH = "README.md"

def get_number_info():
    """numbersapi에서 해당 숫자에 관한 정보를 가져옴"""
    response = requests.get(URL)
    
    if response.status_code == 200:
        return response.text
    else:
        return "정보를 가져오는 데 실패했습니다."

def update_readme():
    """README.md 파일을 업데이트"""
    number_info = get_number_info()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# 연도에 관한 TMI

이 리포지토리는 numbersapi를 사용하여 특정 년도에 관한 TMI를 자동으로 업데이트합니다.

## 연도: ({number_info[:4]})
> {number_info}

⏳ 업데이트 시간: {now} (UTC)

---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()

