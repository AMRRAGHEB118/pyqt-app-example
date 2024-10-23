# app.py
import os

def main():
    egypt_url = os.getenv('EGYPT_URL', 'No EGYPT_URL set')
    dubai_url = os.getenv('DUBAI_URL', 'No DUBAI_URL set')

    print(f"Egypt URL: {egypt_url}")
    print(f"Dubai URL: {dubai_url}")

if __name__ == "__main__":
    main()
