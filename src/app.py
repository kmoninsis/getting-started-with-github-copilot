"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": [
            {"name": "Michael Chen", "email": "michael@mergington.edu"},
            {"name": "Daniel Smith", "email": "daniel@mergington.edu"}
        ]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": [
            {"name": "Emma Johnson", "email": "emma@mergington.edu"},
            {"name": "Sophia Rodriguez", "email": "sophia@mergington.edu"}
        ]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": [
            {"name": "John Williams", "email": "john@mergington.edu"},
            {"name": "Olivia Brown", "email": "olivia@mergington.edu"}
        ]
    },
    "Art Club": {
        "description": "Explore various art techniques and create your own masterpieces",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": [
            {"name": "Ava Davis", "email": "max123@gmail.com"}
        ]
    },
    "Cricket Club": {
        "description": "Learn and play cricket with fellow enthusiasts",
        "schedule": "Saturdays, 10:00 AM - 12:00 PM",
        "max_participants": 15,
        "participants": [
            {"name": "Liam Davis", "email": "liam@mergington.edu"},
            {"name": "Ava Martinez", "email": "ava@mergington.edu"}
        ]
    }

}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student with name and email
    activity["participants"].append({"name": name, "email": email})
    return {"message": f"Signed up {name} ({email}) for {activity_name}"}
