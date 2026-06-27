import requests
import pandas as pd

APP_ID = "c767b891"
APP_KEY = "b0e285332f09df962f8d8b0169283ae5"

def fetch_jobs():

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": "Data Analyst",
        "sort_by": "date"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        print("URL:", response.url)
        print("Status Code:", response.status_code)

        response.raise_for_status()

        data = response.json()

        jobs = []

        if "results" in data:

            for job in data["results"]:

                jobs.append({
                    "title": job.get("title", ""),
                    "company": job.get("company", {}).get("display_name", ""),
                    "description": job.get("description", ""),
                    "apply_link": job.get("redirect_url", ""),
                    "posted_date": job.get("created", "")
                })

        print("Jobs Found:", len(jobs))

        return pd.DataFrame(jobs)

    except Exception as e:

        print("Job Fetch Error:", e)

        return pd.DataFrame()