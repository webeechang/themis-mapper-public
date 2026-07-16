# test_secret.py

def get_github_data():
    # 呢個係一條「假」嘅 GitHub Personal Access Token
    # 用嚟測試 GitHub Advanced Security 嘅 Push Protection 係咪正常運作
    fake_token = "ghp_1234567890abcdefABCDEFGHIJKLMNOPQRST"
    
    print(f"Connecting to GitHub with token: {fake_token}")

if __name__ == "__main__":
    get_github_data()