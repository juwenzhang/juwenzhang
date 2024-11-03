import requests
from github import Github

GITHUB_USER = "juwenzhang"
GITHUB_TOKEN = "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"

github = Github(GITHUB_TOKEN)
user = github.get_user(GITHUB_USER)

repos = user.get_repos()
lang_counter = {}

for repo in repos:
    if repo.language:
        lang_counter[repo.language] = lang_counter.get(repo.language, 0) + 1

total = sum(lang_counter.values())
readme_content = f"## Programming Languages Used

"
for lang, count in lang_counter.items():
    percentage = (count / total) * 100
    readme_content += f"- {lang}: {percentage:.2f}%
"

with open('README.md', 'w') as f:
    f.write(readme_content)