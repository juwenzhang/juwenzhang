import sys
import requests
import os
from github import Github

# 使用环境变量或其他安全方式存储敏感信息
GITHUB_USER = "juwenzhang"
GITHUB_TOKEN =  os.getenv('GITHUB_TOKEN') # 建议使用环境变量

def func():
    try:
        github = Github(GITHUB_TOKEN)
        user = github.get_user(GITHUB_USER)

        repos = user.get_repos()
        lang_counter = {}

        for repo in repos:
            language = repo.language
            if language:
                lang_counter[language] = lang_counter.get(language, 0) + 1
            else:
                lang_counter['Unknown'] = lang_counter.get('Unknown', 0) + 1

        total = sum(lang_counter.values())
        readme_content = "## Programming Languages Used\n\n"

        for lang, count in lang_counter.items():
            percentage = (count / total) * 100
            readme_content += f"- {lang}: {percentage:.2f}%\n"

        with open('README.md', 'w') as f:
            f.write(readme_content)
        print("README.md has been updated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.setrecursionlimit(10)
        func()
func()