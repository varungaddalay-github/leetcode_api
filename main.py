import requests

url = "https://leetcode.com/api/problems/all/"
r = requests.get(url)


if r.status_code == 200:
    data = r.json()

    problems = data['stat_status_pairs']
    company_problems = [problem for problem in problems if 'google'.lower() in problem.get('company_tags', [])]
    print(company_problems)


else:
    print(f'Failed to fetch the questions set. Status code: {r.status_code}')

