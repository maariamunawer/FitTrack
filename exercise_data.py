import random

def get_exercise_recommendations(weight_diff, bmi, sex, age, activity_level):
    """
    Generate personalized exercise recommendations based on user data.
    
    Args:
        weight_diff: Difference between current and goal weight (negative for weight loss)
        bmi: Body Mass Index
        sex: 'male' or 'female'
        age: Age in years
        activity_level: User's activity level
        
    Returns:
        Dictionary containing recommended exercises
    """
    
    # Define exercise categories
    cardio_exercises = [
        {
            "name": "Brisk Walking",
            "description": "A low-impact cardio exercise good for beginners.",
            "duration": "30-45 minutes",
            "frequency": "5-7 days per week",
            "intensity": "Moderate",
            "calories_burned": "150-300 calories",
            "image_url": "https://images.unsplash.com/photo-1483721310020-03333e577078"
        },
        {
            "name": "Cycling",
            "description": "Excellent low-impact cardio that strengthens lower body.",
            "duration": "30-60 minutes",
            "frequency": "3-5 days per week",
            "intensity": "Moderate to High",
            "calories_burned": "300-600 calories",
            "image_url": "https://images.unsplash.com/photo-1518644961665-ed172691aaa1"
        },
        {
            "name": "Swimming",
            "description": "Full-body workout that's gentle on joints.",
            "duration": "30-45 minutes",
            "frequency": "2-4 days per week",
            "intensity": "Moderate to High",
            "calories_burned": "400-700 calories",
            "image_url": "https://images.unsplash.com/photo-1464925257126-6450e871c667"
        },
        {
            "name": "Running",
            "description": "High-intensity cardio that burns calories efficiently.",
            "duration": "20-40 minutes",
            "frequency": "3-4 days per week",
            "intensity": "High",
            "calories_burned": "400-800 calories",
            "image_url": "https://images.unsplash.com/photo-1518310383802-640c2de311b2"
        },
        {
            "name": "Jumping Rope",
            "description": "Simple but effective cardio workout.",
            "duration": "15-30 minutes",
            "frequency": "3-5 days per week",
            "intensity": "High",
            "calories_burned": "200-400 calories",
            "image_url": "https://images.unsplash.com/photo-1518644961665-ed172691aaa1"
        }
    ]
    
    strength_exercises = [
        {
            "name": "Bodyweight Squats",
            "description": "Basic lower body exercise targeting quads, hamstrings and glutes.",
            "sets": "3-4 sets",
            "reps": "12-15 reps",
            "frequency": "2-3 days per week",
            "intensity": "Low to Moderate",
            "image_url": "https://images.unsplash.com/photo-1518459031867-a89b944bffe4"
        },
        {
            "name": "Push-ups",
            "description": "Classic upper body exercise for chest, shoulders and triceps.",
            "sets": "3-4 sets",
            "reps": "10-15 reps",
            "frequency": "2-3 days per week",
            "intensity": "Moderate",
            "image_url": "https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5"
        },
        {
            "name": "Planks",
            "description": "Core strengthening isometric exercise.",
            "sets": "3 sets",
            "reps": "30-60 seconds",
            "frequency": "3-4 days per week",
            "intensity": "Moderate",
            "image_url": "https://images.unsplash.com/photo-1518611012118-696072aa579a"
        },
        {
            "name": "Dumbbell Rows",
            "description": "Upper back and bicep strengthening exercise.",
            "sets": "3 sets",
            "reps": "10-12 reps per side",
            "frequency": "2 days per week",
            "intensity": "Moderate",
            "image_url": "https://images.unsplash.com/photo-1518644961665-ed172691aaa1"
        },
        {
            "name": "Lunges",
            "description": "Lower body exercise for balance and strength.",
            "sets": "3 sets",
            "reps": "10-12 reps per leg",
            "frequency": "2-3 days per week",
            "intensity": "Moderate",
            "image_url": "https://images.unsplash.com/photo-1483721310020-03333e577078"
        }
    ]
    
    flexibility_exercises = [
        {
            "name": "Yoga",
            "description": "Combines strength, flexibility and mindfulness.",
            "duration": "20-60 minutes",
            "frequency": "3-7 days per week",
            "intensity": "Low to Moderate",
            "focus": "Full body flexibility and relaxation",
            "image_url": "https://images.unsplash.com/photo-1518611012118-696072aa579a"
        },
        {
            "name": "Dynamic Stretching",
            "description": "Active stretches that prepare muscles for exercise.",
            "duration": "5-10 minutes",
            "frequency": "Before each workout",
            "intensity": "Low",
            "focus": "Warming up muscles and joints",
            "image_url": "https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5"
        },
        {
            "name": "Static Stretching",
            "description": "Held stretches to improve flexibility.",
            "duration": "10-15 minutes",
            "frequency": "After workouts or daily",
            "intensity": "Low",
            "focus": "Improving range of motion",
            "image_url": "https://images.unsplash.com/photo-1518459031867-a89b944bffe4"
        }
    ]
    
    # Determine goal type
    if weight_diff < 0:
        goal_type = "weight_loss"
    elif weight_diff > 0:
        goal_type = "weight_gain"
    else:
        goal_type = "maintenance"
    
    # Tailor exercise recommendations based on user data
    recommendations = {"cardio": [], "strength": [], "flexibility": []}
    
    # For beginners (based on activity level)
    if activity_level in ['sedentary', 'light']:
        beginner_cardio = [ex for ex in cardio_exercises if ex["name"] in ["Brisk Walking", "Swimming", "Cycling"]]
        beginner_strength = [ex for ex in strength_exercises if ex["name"] in ["Bodyweight Squats", "Push-ups", "Planks"]]
        beginner_flexibility = [ex for ex in flexibility_exercises if ex["name"] in ["Static Stretching", "Dynamic Stretching"]]
        
        recommendations["cardio"] = random.sample(beginner_cardio, min(2, len(beginner_cardio)))
        recommendations["strength"] = random.sample(beginner_strength, min(2, len(beginner_strength)))
        recommendations["flexibility"] = random.sample(beginner_flexibility, min(1, len(beginner_flexibility)))
    
    # For intermediate/advanced (based on activity level)
    else:
        if goal_type == "weight_loss":
            # Prioritize cardio for weight loss
            recommendations["cardio"] = random.sample(cardio_exercises, min(3, len(cardio_exercises)))
            recommendations["strength"] = random.sample(strength_exercises, min(2, len(strength_exercises)))
        elif goal_type == "weight_gain":
            # Prioritize strength for weight gain (muscle mass)
            recommendations["cardio"] = random.sample(cardio_exercises, min(1, len(cardio_exercises)))
            recommendations["strength"] = random.sample(strength_exercises, min(3, len(strength_exercises)))
        else:
            # Balanced approach for maintenance
            recommendations["cardio"] = random.sample(cardio_exercises, min(2, len(cardio_exercises)))
            recommendations["strength"] = random.sample(strength_exercises, min(2, len(strength_exercises)))
        
        recommendations["flexibility"] = random.sample(flexibility_exercises, min(1, len(flexibility_exercises)))
    
    # Special considerations
    # For older adults (50+), add more low-impact options
    if age > 50:
        # Replace high-impact with low-impact options
        for i, exercise in enumerate(recommendations["cardio"]):
            if exercise["name"] == "Running" or exercise["name"] == "Jumping Rope":
                low_impact = [ex for ex in cardio_exercises if ex["name"] in ["Brisk Walking", "Swimming", "Cycling"]]
                if low_impact:
                    recommendations["cardio"][i] = random.choice(low_impact)
    
    # For high BMI, focus on joint-friendly exercises
    if bmi > 30:
        # Replace high-impact with low-impact options
        for i, exercise in enumerate(recommendations["cardio"]):
            if exercise["name"] == "Running" or exercise["name"] == "Jumping Rope":
                joint_friendly = [ex for ex in cardio_exercises if ex["name"] in ["Swimming", "Cycling"]]
                if joint_friendly:
                    recommendations["cardio"][i] = random.choice(joint_friendly)
    
    # Flatten the recommendations for easier use in templates
    flattened_recommendations = []
    for category, exercises in recommendations.items():
        for exercise in exercises:
            exercise["category"] = category
            flattened_recommendations.append(exercise)
    
    # Add weekly schedule recommendation
    if goal_type == "weight_loss":
        schedule = {
            "Monday": "Cardio (30-45 min) + Core Strength",
            "Tuesday": "Strength Training (Full Body)",
            "Wednesday": "Active Recovery (Walking or Light Cardio)",
            "Thursday": "High-Intensity Cardio (20-30 min)",
            "Friday": "Strength Training (Upper Body Focus)",
            "Saturday": "Cardio (30-45 min) + Strength (Lower Body Focus)",
            "Sunday": "Rest or Light Activity (Stretching/Yoga)"
        }
    elif goal_type == "weight_gain":
        schedule = {
            "Monday": "Strength Training (Upper Body)",
            "Tuesday": "Light Cardio (20 min) + Core",
            "Wednesday": "Strength Training (Lower Body)",
            "Thursday": "Rest or Active Recovery",
            "Friday": "Strength Training (Full Body)",
            "Saturday": "Moderate Cardio + Flexibility",
            "Sunday": "Rest"
        }
    else:  # maintenance
        schedule = {
            "Monday": "Cardio (30 min) + Core",
            "Tuesday": "Strength Training (Upper Body)",
            "Wednesday": "Moderate Cardio or Active Recovery",
            "Thursday": "Strength Training (Lower Body)",
            "Friday": "Flexibility + Light Cardio",
            "Saturday": "Mixed Workout (Cardio + Strength)",
            "Sunday": "Rest or Light Activity"
        }
    
    return {
        "exercises": flattened_recommendations,
        "schedule": schedule
    }


def calculate_water_intake(weight, activity_level):
    """
    Calculate recommended daily water intake based on weight and activity level.
    
    Args:
        weight: Weight in kg
        activity_level: User's activity level
        
    Returns:
        Recommended water intake in liters
    """
    # Base calculation: 35ml per kg of body weight
    base_intake = weight * 35
    
    # Adjust for activity level
    activity_factors = {
        'sedentary': 1.0,
        'light': 1.1,
        'moderate': 1.2,
        'active': 1.3,
        'very_active': 1.4
    }
    
    adjusted_intake = base_intake * activity_factors[activity_level]
    
    # Convert to liters and round to 1 decimal place
    return round(adjusted_intake / 1000, 1)


def get_diet_recommendations(goal_type, calorie_target):
    """
    Generate personalized diet recommendations based on user goals.
    
    Args:
        goal_type: 'loss', 'gain', or 'maintain'
        calorie_target: Daily calorie target
        
    Returns:
        Dictionary containing diet recommendations
    """
    # Define macronutrient ratios based on goal
    if goal_type == 'loss':
        protein_ratio = 0.35  # 35% protein
        fat_ratio = 0.25      # 25% fat
        carb_ratio = 0.40     # 40% carbs
    elif goal_type == 'gain':
        protein_ratio = 0.30  # 30% protein
        fat_ratio = 0.25      # 25% fat
        carb_ratio = 0.45     # 45% carbs
    else:  # maintain
        protein_ratio = 0.30  # 30% protein
        fat_ratio = 0.30      # 30% fat
        carb_ratio = 0.40     # 40% carbs
    
    # Calculate macros in grams
    protein_calories = calorie_target * protein_ratio
    fat_calories = calorie_target * fat_ratio
    carb_calories = calorie_target * carb_ratio
    
    protein_grams = round(protein_calories / 4)  # 4 calories per gram of protein
    fat_grams = round(fat_calories / 9)          # 9 calories per gram of fat
    carb_grams = round(carb_calories / 4)        # 4 calories per gram of carbs
    
    # Define meal plan structure
    meal_structure = {
        'breakfast': {
            'portion': 0.25,  # 25% of daily calories
            'description': 'Start your day with a balanced breakfast to fuel your morning activities.',
            'image_url': 'https://images.unsplash.com/photo-1504754524776-8f4f37790ca0'
        },
        'lunch': {
            'portion': 0.35,  # 35% of daily calories
            'description': 'A substantial midday meal to maintain energy levels throughout the afternoon.',
            'image_url': 'https://images.unsplash.com/photo-1447078806655-40579c2520d6'
        },
        'dinner': {
            'portion': 0.30,  # 30% of daily calories
            'description': 'A satisfying evening meal that aligns with your nutritional goals.',
            'image_url': 'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578'
        },
        'snacks': {
            'portion': 0.10,  # 10% of daily calories
            'description': 'Healthy snacks between meals to maintain energy and control hunger.',
            'image_url': 'https://images.unsplash.com/photo-1518635017498-87f514b751ba'
        }
    }
    
    # Calculate calories for each meal
    for meal, data in meal_structure.items():
        data['calories'] = round(calorie_target * data['portion'])
    
    # Food recommendations based on goal
    food_recommendations = {
        'protein_sources': [
            {'name': 'Chicken Breast', 'info': 'Lean protein source, low in fat, high in protein.'},
            {'name': 'Greek Yogurt', 'info': 'High protein dairy option, good for snacks or breakfast.'},
            {'name': 'Eggs', 'info': 'Complete protein source with essential nutrients.'},
            {'name': 'Tofu', 'info': 'Plant-based protein option, versatile for many dishes.'},
            {'name': 'Fish', 'info': 'Lean protein with healthy omega-3 fatty acids.'}
        ],
        'carb_sources': [
            {'name': 'Brown Rice', 'info': 'Whole grain option with more fiber than white rice.'},
            {'name': 'Sweet Potatoes', 'info': 'Nutrient-dense complex carbohydrate.'},
            {'name': 'Quinoa', 'info': 'Complete protein and complex carb source.'},
            {'name': 'Oats', 'info': 'Fiber-rich breakfast option that helps with satiety.'},
            {'name': 'Whole Grain Bread', 'info': 'Better option than refined white bread.'}
        ],
        'fat_sources': [
            {'name': 'Avocado', 'info': 'Healthy monounsaturated fats and fiber.'},
            {'name': 'Nuts', 'info': 'Healthy fats, protein, and fiber in a convenient package.'},
            {'name': 'Olive Oil', 'info': 'Healthy cooking oil rich in monounsaturated fats.'},
            {'name': 'Chia Seeds', 'info': 'Omega-3 fatty acids and fiber.'},
            {'name': 'Fatty Fish', 'info': 'Salmon and mackerel provide protein and omega-3s.'}
        ],
        'vegetables': [
            {'name': 'Leafy Greens', 'info': 'Spinach, kale, etc. - low calorie, nutrient-dense options.'},
            {'name': 'Broccoli', 'info': 'High in fiber, vitamins, and has some protein.'},
            {'name': 'Bell Peppers', 'info': 'High in vitamin C and adds color to meals.'},
            {'name': 'Cauliflower', 'info': 'Versatile vegetable that can substitute for higher-carb options.'},
            {'name': 'Zucchini', 'info': 'Low in calories, can be used in many dishes.'}
        ],
        'fruits': [
            {'name': 'Berries', 'info': 'Lower in sugar than many fruits, high in antioxidants.'},
            {'name': 'Apples', 'info': 'Portable, filling, and contain fiber.'},
            {'name': 'Citrus Fruits', 'info': 'High in vitamin C and other nutrients.'},
            {'name': 'Bananas', 'info': 'Good source of potassium and convenient pre/post workout.'},
            {'name': 'Pears', 'info': 'High in fiber and water content.'}
        ]
    }
    
    # Example meals based on goal
    meal_examples = {
        'breakfast': get_meal_example('breakfast', goal_type),
        'lunch': get_meal_example('lunch', goal_type),
        'dinner': get_meal_example('dinner', goal_type),
        'snacks': get_meal_example('snacks', goal_type)
    }
    
    # Nutrition tips based on goal
    if goal_type == 'loss':
        tips = [
            'Focus on protein-rich foods to maintain muscle while losing fat',
            'Include fiber-rich vegetables to help you feel full on fewer calories',
            'Drink water before meals to help control portion sizes',
            'Limit processed foods and added sugars',
            'Consider intermittent fasting if it works with your lifestyle',
            'Plan meals ahead to avoid impulsive high-calorie choices'
        ]
    elif goal_type == 'gain':
        tips = [
            'Eat more frequently throughout the day (5-6 smaller meals)',
            'Prioritize calorie-dense foods like nuts, avocados, and healthy oils',
            'Consume protein before and after workouts to support muscle growth',
            'Include liquid calories like smoothies for easier consumption',
            'Focus on nutrient-dense foods rather than empty calories',
            'Gradually increase portions to avoid digestive discomfort'
        ]
    else:  # maintain
        tips = [
            'Balance your macronutrients for optimal health and energy',
            'Practice mindful eating - pay attention to hunger and fullness cues',
            'Adjust your calories based on activity levels each day',
            'Include a variety of foods to ensure proper nutrient intake',
            'Limit ultra-processed foods in favor of whole food options',
            'Consider meal prep to maintain consistency throughout the week'
        ]
    
    return {
        'macros': {
            'protein': protein_grams,
            'fat': fat_grams,
            'carbs': carb_grams
        },
        'meal_structure': meal_structure,
        'food_recommendations': food_recommendations,
        'meal_examples': meal_examples,
        'tips': tips
    }


def get_meal_example(meal_type, goal_type):
    """Helper function to get example meals based on meal type and goal"""
    examples = {
        'loss': {
            'breakfast': 'Greek yogurt with berries and a tablespoon of chia seeds',
            'lunch': 'Grilled chicken salad with mixed greens, cherry tomatoes, cucumber, and light vinaigrette',
            'dinner': 'Baked salmon with steamed broccoli and a small portion of quinoa',
            'snacks': 'Apple slices with a tablespoon of natural almond butter'
        },
        'gain': {
            'breakfast': 'Oatmeal made with milk, topped with banana, nuts, and a scoop of protein powder',
            'lunch': 'Turkey and avocado sandwich on whole grain bread with a side of sweet potato wedges',
            'dinner': 'Lean steak with roasted vegetables and brown rice',
            'snacks': 'Protein smoothie with milk, banana, peanut butter, and protein powder'
        },
        'maintain': {
            'breakfast': 'Two eggs with whole grain toast and half an avocado',
            'lunch': 'Tuna wrap with mixed vegetables and a side of fruit',
            'dinner': 'Stir-fried chicken and vegetables with a moderate portion of brown rice',
            'snacks': 'A small handful of mixed nuts and a piece of fruit'
        }
    }
    
    return examples[goal_type][meal_type]