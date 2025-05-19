from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'
DATA_FILE = 'events.json'

def load_events():
    """Load events from JSON file, create if not exists"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_events(events):
    """Save events to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(events, f, indent=2)

def check_conflict(new_start, new_end):
    """Check for time conflicts"""
    events = load_events()
    new_start = datetime.fromisoformat(new_start)
    new_end = datetime.fromisoformat(new_end)
    
    for event in events:
        existing_start = datetime.fromisoformat(event['start'])
        existing_end = datetime.fromisoformat(event['end'])
        if (new_start < existing_end) and (new_end > existing_start):
            return True
    return False

@app.route('/')
def home():
    """Home page with events"""
    events = sorted(load_events(), key=lambda x: x['start'])
    print(f"DEBUG: Loaded {len(events)} events")  # Debug line
    return render_template('index.html', 
                         events=events,
                         datetime=datetime,
                         check_conflict=check_conflict)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Add new event"""
    if request.method == 'POST':
        event_data = {
            'id': str(datetime.now().timestamp()),
            'title': request.form['title'],
            'start': request.form['start'],
            'end': request.form['end'],
            'category': request.form['category'],
            'description': request.form.get('description', '')
        }
        
        if check_conflict(event_data['start'], event_data['end']):
            flash('⛔ Time conflict detected!', 'danger')
            return redirect(url_for('add_event'))
        
        events = load_events()
        events.append(event_data)
        save_events(events)
        flash('✅ Event added successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('add.html')

@app.route('/delete/<event_id>', methods=['POST'])
def delete_event(event_id):
    """Delete event"""
    events = [e for e in load_events() if e['id'] != event_id]
    save_events(events)
    flash('🗑️ Event deleted', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)