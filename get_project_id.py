 
import requests
from requests.auth import HTTPBasicAuth
# Constants
PROJECT_ID = "sample"  # Replace with your actual project ID
BASE_URL = f"https://anblicks.openproject.com/api/v3/projects/{PROJECT_ID}/work_packages"
API_KEY = "cce9ce739e074955f0ac90def1d1affd8236086eb8896600943186d49dd75386"
# Headers for API calls
HEADERS = {
    "Content-Type": "application/json"
}

def get_all_work_package_ids():
    """Fetch all work packages associated with the user."""
    # url = f"{BASE_URL}/work_packages"
    response = requests.get(BASE_URL, headers=HEADERS, auth=HTTPBasicAuth('apikey', API_KEY))
    if response.status_code == 200:
        work_packages = response.json()["_embedded"]["elements"]
        print(f"Found {len(work_packages)} work packages:")
        wp_ids=[]
        for wp in work_packages:
            wp_ids.append(wp['id'])
            #print(f"\nID: {wp['id']}")
            # print(f"Subject: {wp['subject']}")
            # print(f"Description: {wp.get('description', {}).get('raw', 'No description')}")
            # print(f"Status: {wp['_links']['status']['title']}")
            # print(f"Priority: {wp['_links']['priority']['title']}")
            # print(f"Assignee: {wp['_links'].get('assignee', {}).get('title', 'Unassigned')}")
            # print(f"Type: {wp['_links']['type']['title']}")
            # print(f"Project: {wp['_links']['project']['title']}")
        return wp_ids
    else:
        print("Failed to fetch work packages:", response.status_code, response.text)

def get_all_work_package_title(work_package_id):
    """Fetch all work packages associated with the user."""
    # url = f"{BASE_URL}/work_packages"
    response = requests.get(BASE_URL, headers=HEADERS, auth=HTTPBasicAuth('apikey', API_KEY))
    if response.status_code == 200:
        work_packages = response.json()["_embedded"]["elements"]
        print(f"Found {len(work_packages)} work packages:")
        wp_subjects=[]
        for wp in work_packages:
            if wp["id"] == work_package_id:
                # print("\nWork Package Found:")
                # print(f"ID: {wp['id']}")
                return wp['subject']
            #print(f"\nID: {wp['id']}")
            # print(f"Subject: {wp['subject']}")
            # print(f"Description: {wp.get('description', {}).get('raw', 'No description')}")
            # print(f"Status: {wp['_links']['status']['title']}")
            # print(f"Priority: {wp['_links']['priority']['title']}")
            # print(f"Assignee: {wp['_links'].get('assignee', {}).get('title', 'Unassigned')}")
            # print(f"Type: {wp['_links']['type']['title']}")
            # print(f"Project: {wp['_links']['project']['title']}")
        return wp_subjects
    else:
        print("Failed to fetch work packages:", response.status_code, response.text)


def get_all_work_package_description(work_package_id):
    """Fetch all work packages associated with the user."""
    # url = f"{BASE_URL}/work_packages"
    response = requests.get(BASE_URL, headers=HEADERS, auth=HTTPBasicAuth('apikey', API_KEY))
    if response.status_code == 200:
        work_packages = response.json()["_embedded"]["elements"]
        #print(f"Found {len(work_packages)} work packages:")
        wp_subjects=[]
        for wp in work_packages:
            if wp["id"] == work_package_id:
                # print("\nWork Package Found:")
                # print(f"ID: {wp['id']}")
                return wp.get('description', {}).get('raw', 'No description')
        return wp_subjects
    else:
        print("Failed to fetch work packages:", response.status_code, response.text)