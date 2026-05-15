# Jumeirah Park — Villa Property Lookup

A Streamlit web app to search and view full property details for any villa in Jumeirah Park, Dubai.

## Files in this folder

| File | Purpose |
|---|---|
| `app.py` | The Streamlit app |
| `requirements.txt` | Python dependencies |
| `master_villa_db.csv` | The master property database (you add this) |

---

## How to deploy (step by step)

### Step 1 — Create a GitHub account
Go to https://github.com and sign up (free).

### Step 2 — Create a new repository
1. Click the **+** icon → **New repository**
2. Name it: `jumeirah-park-lookup`
3. Set it to **Public**
4. Click **Create repository**

### Step 3 — Upload the files
In your new repository:
1. Click **Add file** → **Upload files**
2. Upload all 3 files:
   - `app.py`
   - `requirements.txt`
   - `master_villa_db.csv`
3. Click **Commit changes**

### Step 4 — Update the CSV URL in app.py
In `app.py`, find this line:

```python
url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/master_villa_db.csv"
```

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPO` with `jumeirah-park-lookup`.

For example:
```python
url = "https://raw.githubusercontent.com/noman123/jumeirah-park-lookup/main/master_villa_db.csv"
```

Commit the change.

### Step 5 — Deploy on Streamlit Cloud
1. Go to https://streamlit.io/cloud and sign in with your GitHub account
2. Click **New app**
3. Select your repository: `jumeirah-park-lookup`
4. Main file path: `app.py`
5. Click **Deploy**

Streamlit will build and launch your app in ~2 minutes.
You'll get a URL like: `https://noman123-jumeirah-park-lookup-app-xxxx.streamlit.app`

Share that link with anyone — no login, no install, works on phone and desktop.

---

## Updating the data
When you have new data, just replace `master_villa_db.csv` in GitHub with the new file.
The app will automatically reload with the latest data within a minute.
