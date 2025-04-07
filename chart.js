/**
 * Chart.js Integration for FitTrack
 * This file contains the Chart.js setup and configurations
 */

// Progress Chart - to visualize weight progress over time
function createProgressChart(currentWeight, goalWeight) {
    const ctx = document.getElementById('progressChart');
    
    if (!ctx) return; // Exit if canvas doesn't exist
    
    const weightDiff = goalWeight - currentWeight;
    const isWeightLoss = weightDiff < 0;
    const absWeightDiff = Math.abs(weightDiff);
    
    // Generate future weight data points (weekly projections)
    // Assuming 0.5kg/week weight change
    const weeks = Math.ceil(absWeightDiff / 0.5);
    const labels = [];
    const data = [];
    
    // Add current week
    labels.push('Now');
    data.push(currentWeight);
    
    // Generate future weeks
    for (let i = 1; i <= weeks; i++) {
        labels.push(`Week ${i}`);
        const weeklyChange = isWeightLoss ? -0.5 : 0.5;
        data.push(Math.round((currentWeight + (weeklyChange * i)) * 10) / 10);
    }
    
    // Add goal
    labels.push('Goal');
    data.push(goalWeight);
    
    // Chart colors
    const primaryColor = '#64b5f6';
    const secondaryColor = '#81c784';
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Weight Progress',
                data: data,
                borderColor: primaryColor,
                backgroundColor: 'rgba(100, 181, 246, 0.1)',
                pointBackgroundColor: primaryColor,
                pointRadius: 5,
                pointHoverRadius: 7,
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Weight: ${context.raw}kg`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    title: {
                        display: true,
                        text: 'Weight (kg)'
                    },
                    suggestedMin: Math.min(currentWeight, goalWeight) - 2,
                    suggestedMax: Math.max(currentWeight, goalWeight) + 2
                }
            }
        }
    });
}

// Calorie Breakdown Chart
function createCalorieChart(caloricTarget) {
    const ctx = document.getElementById('calorieChart');
    
    if (!ctx) return; // Exit if canvas doesn't exist
    
    // Split caloric target into meals
    const breakfast = Math.round(caloricTarget * 0.25);
    const lunch = Math.round(caloricTarget * 0.35);
    const dinner = Math.round(caloricTarget * 0.30);
    const snacks = Math.round(caloricTarget * 0.10);
    
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Breakfast', 'Lunch', 'Dinner', 'Snacks'],
            datasets: [{
                data: [breakfast, lunch, dinner, snacks],
                backgroundColor: [
                    '#64b5f6', // Breakfast
                    '#81c784', // Lunch
                    '#9575cd', // Dinner
                    '#ffb74d'  // Snacks
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'right'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label;
                            const value = context.raw;
                            const total = context.dataset.data.reduce((acc, val) => acc + val, 0);
                            const percentage = Math.round((value / total) * 100);
                            return `${label}: ${value} calories (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

// Water Consumption Progress Chart
function createWaterChart(recommendedWater) {
    const ctx = document.getElementById('waterProgressChart');
    
    if (!ctx) return; // Exit if canvas doesn't exist
    
    // Convert to milliliters for more detail
    const recommendedMl = recommendedWater * 1000;
    
    // Create hourly breakdown (assuming 16 waking hours)
    const hours = ['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm'];
    
    // Create ideal water consumption pattern throughout the day
    const idealConsumption = [];
    let cumulativeAmount = 0;
    
    // Higher consumption in morning and early afternoon
    for (let i = 0; i < hours.length; i++) {
        let hourlyAmount;
        
        if (i < 4) { // Morning (8am-12pm)
            hourlyAmount = recommendedMl * 0.1;
        } else if (i < 8) { // Early afternoon (12pm-4pm)
            hourlyAmount = recommendedMl * 0.08;
        } else if (i < 12) { // Late afternoon/early evening (4pm-8pm)
            hourlyAmount = recommendedMl * 0.06;
        } else { // Evening (8pm-12am)
            hourlyAmount = recommendedMl * 0.03;
        }
        
        cumulativeAmount += hourlyAmount;
        idealConsumption.push(Math.round(cumulativeAmount / 1000 * 10) / 10); // Convert back to liters with 1 decimal
    }
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: hours,
            datasets: [{
                label: 'Ideal Water Consumption',
                data: idealConsumption,
                borderColor: '#64b5f6',
                backgroundColor: 'rgba(100, 181, 246, 0.2)',
                pointBackgroundColor: '#64b5f6',
                pointRadius: 4,
                pointHoverRadius: 6,
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Water: ${context.raw}L`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    title: {
                        display: true,
                        text: 'Water (Liters)'
                    },
                    min: 0,
                    max: Math.ceil(recommendedWater)
                }
            }
        }
    });
}