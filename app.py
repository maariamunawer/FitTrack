import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import pandas as pd
import numpy as np
from exercise_data import get_exercise_recommendations, calculate_water_intake, get_diet_recommendations

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

@app.route('/')
def index():
    """Render the home page with the input form"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Process user input and store in session"""
    try:
        # Get user input
        age = int(request.form.get('age'))
        weight = float(request.form.get('weight'))
        goal_weight = float(request.form.get('goal_weight'))
        sex = request.form.get('sex')
        height = float(request.form.get('height'))
        activity_level = request.form.get('activity_level')
        
        # Validate input
        if age < 12 or age > 100:
            flash('Please enter a valid age between 12 and 100.')
            return redirect(url_for('index'))
        
        if weight < 30 or weight > 300:
            flash('Please enter a valid weight between 30kg and 300kg.')
            return redirect(url_for('index'))
            
        if goal_weight < 30 or goal_weight > 300:
            flash('Please enter a valid goal weight between 30kg and 300kg.')
            return redirect(url_for('index'))
            
        if height < 100 or height > 250:
            flash('Please enter a valid height between 100cm and 250cm.')
            return redirect(url_for('index'))
        
        # Store in session
        session['user_data'] = {
            'age': age,
            'weight': weight,
            'goal_weight': goal_weight,
            'sex': sex,
            'height': height,
            'activity_level': activity_level
        }
        
        # Calculate BMI
        bmi = weight / ((height/100) ** 2)
        session['bmi'] = round(bmi, 2)
        
        # Calculate BMR (Basal Metabolic Rate) using Mifflin-St Jeor Equation
        if sex == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        
        # Calculate TDEE (Total Daily Energy Expenditure)
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        
        tdee = bmr * activity_factors[activity_level]
        session['tdee'] = round(tdee)
        
        # Calculate water intake
        water_intake = calculate_water_intake(weight, activity_level)
        session['water_intake'] = water_intake
        
        # Calculate calorie deficit/surplus based on goal
        weight_diff = goal_weight - weight
        
        # Calculate daily calorie target (assuming ~500 calorie deficit/surplus for ~0.5kg/week)
        if weight_diff < 0:  # Weight loss
            session['calorie_target'] = max(1200, round(tdee - 500))
            session['goal_type'] = 'loss'
        elif weight_diff > 0:  # Weight gain
            session['calorie_target'] = round(tdee + 500)
            session['goal_type'] = 'gain'
        else:  # Maintenance
            session['calorie_target'] = round(tdee)
            session['goal_type'] = 'maintain'
            
        # Get exercise recommendations
        session['exercises'] = get_exercise_recommendations(
            weight_diff, 
            bmi, 
            sex, 
            age,
            activity_level
        )
        
        # Get diet recommendations
        session['diet'] = get_diet_recommendations(
            session['goal_type'],
            session['calorie_target']
        )
        
        # Calculate weeks to goal
        if weight_diff != 0:
            # Assumes 0.5kg/week weight change with a 500 calorie deficit/surplus
            weeks_to_goal = abs(weight_diff) / 0.5
            session['weeks_to_goal'] = round(weeks_to_goal)
        else:
            session['weeks_to_goal'] = 0
            
        return redirect(url_for('dashboard'))
        
    except Exception as e:
        app.logger.error(f"Error processing form: {str(e)}")
        flash('There was an error processing your information. Please try again.')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """Display personalized recommendations dashboard"""
    if 'user_data' not in session:
        flash('Please enter your information first.')
        return redirect(url_for('index'))
        
    return render_template(
        'dashboard.html',
        user_data=session['user_data'],
        bmi=session['bmi'],
        tdee=session['tdee'],
        calorie_target=session['calorie_target'],
        water_intake=session['water_intake'],
        exercises=session['exercises'],
        diet=session['diet'],
        goal_type=session['goal_type'],
        weeks_to_goal=session['weeks_to_goal']
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)