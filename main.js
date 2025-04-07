/*
 * Main JavaScript for FitTrack- Exercise Recommendation Website
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    
    // Initialize form validation
    initFormValidation();
    
    // Initialize water tracker if on dashboard page
    if (document.querySelector('.water-glass')) {
        initWaterTracker();
    }
    
    // Initialize tooltips
    initTooltips();
    
    // Initialize BMI visualization if present
    if (document.getElementById('bmiChart')) {
        initBMIChart();
    }
    
    // Initialize macro nutrients chart if present
    if (document.getElementById('macroChart')) {
        initMacroChart();
    }
});

/**
 * Initialize fade-in animations
 */
function initAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');
    
    fadeElements.forEach(element => {
        // Make sure elements are visible after animation completes
        // This helps if JavaScript fails to trigger the animation
        setTimeout(() => {
            element.style.opacity = '1';
        }, 1000);
    });
}

/**
 * Basic form validation
 */
function initFormValidation() {
    const form = document.getElementById('user-info-form');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            const age = document.getElementById('age').value;
            const weight = document.getElementById('weight').value;
            const goalWeight = document.getElementById('goal_weight').value;
            const height = document.getElementById('height').value;
            
            let isValid = true;
            let errorMessage = '';
            
            // Basic validation
            if (age < 12 || age > 100) {
                errorMessage += 'Please enter a valid age between 12 and 100. ';
                isValid = false;
            }
            
            if (weight < 30 || weight > 300) {
                errorMessage += 'Please enter a valid weight between 30kg and 300kg. ';
                isValid = false;
            }
            
            if (goalWeight < 30 || goalWeight > 300) {
                errorMessage += 'Please enter a valid goal weight between 30kg and 300kg. ';
                isValid = false;
            }
            
            if (height < 100 || height > 250) {
                errorMessage += 'Please enter a valid height between 100cm and 250cm.';
                isValid = false;
            }
            
            if (!isValid) {
                event.preventDefault();
                showAlert(errorMessage, 'error');
            }
        });
    }
}

/**
 * Display alert messages
 */
function showAlert(message, type = 'error') {
    const alertsContainer = document.getElementById('alerts-container');
    
    if (alertsContainer) {
        const alertElement = document.createElement('div');
        alertElement.className = type === 'error' ? 'alert alert-error' : 'alert alert-success';
        alertElement.textContent = message;
        
        alertsContainer.appendChild(alertElement);
        
        // Auto-remove alert after 5 seconds
        setTimeout(() => {
            alertElement.remove();
        }, 5000);
    }
}

/**
 * Initialize water tracker visualization
 */
function initWaterTracker() {
    const waterFill = document.querySelector('.water-fill');
    const waterPercentage = document.querySelector('.water-percentage');
    const recommendedIntake = parseFloat(document.getElementById('recommended-water').dataset.liters);
    
    if (waterFill && waterPercentage && recommendedIntake) {
        // Animate water fill from 0 to recommended value
        let currentIntake = 0;
        const animationDuration = 1500; // ms
        const steps = 50;
        const increment = recommendedIntake / steps;
        const stepTime = animationDuration / steps;
        
        const animation = setInterval(() => {
            currentIntake += increment;
            
            if (currentIntake >= recommendedIntake) {
                currentIntake = recommendedIntake;
                clearInterval(animation);
            }
            
            // Update water fill height (80% max to leave some space at top of glass)
            const fillPercentage = (currentIntake / recommendedIntake) * 80;
            waterFill.style.height = fillPercentage + '%';
            
            // Update percentage text
            waterPercentage.textContent = currentIntake.toFixed(1) + 'L';
        }, stepTime);
    }
}

/**
 * Initialize tooltips for information icons
 */
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', (e) => {
            const tipText = e.target.getAttribute('data-tooltip');
            
            // Create tooltip element
            const tipElement = document.createElement('div');
            tipElement.className = 'tooltip';
            tipElement.textContent = tipText;
            
            // Position tooltip
            document.body.appendChild(tipElement);
            const rect = e.target.getBoundingClientRect();
            tipElement.style.top = rect.top - tipElement.offsetHeight - 10 + 'px';
            tipElement.style.left = rect.left + (rect.width / 2) - (tipElement.offsetWidth / 2) + 'px';
            tipElement.style.opacity = '1';
            
            // Store reference to the tooltip
            e.target._tooltip = tipElement;
        });
        
        tooltip.addEventListener('mouseleave', (e) => {
            if (e.target._tooltip) {
                e.target._tooltip.remove();
                e.target._tooltip = null;
            }
        });
    });
}

/**
 * BMI Chart using Chart.js
 */
function initBMIChart() {
    const ctx = document.getElementById('bmiChart').getContext('2d');
    const userBMI = parseFloat(document.getElementById('bmiChart').dataset.bmi);
    
    // BMI categories
    const categories = [
        { label: 'Underweight', limit: 18.5, color: '#FFC107' },
        { label: 'Normal', limit: 24.9, color: '#4CAF50' },
        { label: 'Overweight', limit: 29.9, color: '#FF9800' },
        { label: 'Obese', limit: 100, color: '#F44336' }
    ];
    
    // Find user's category
    let userCategory = 'Underweight';
    for (let i = 0; i < categories.length; i++) {
        if (userBMI <= categories[i].limit) {
            userCategory = categories[i].label;
            break;
        }
    }
    
    // Create chart data
    const labels = categories.map(c => c.label);
    const data = [16, 21.7, 27.5, 35]; // Representative values for each category
    const colors = categories.map(c => c.color);
    const userIndex = labels.indexOf(userCategory);
    
    const backgroundColors = colors.map((color, index) => 
        index === userIndex ? color : color + '80' // Add transparency to non-user categories
    );
    
    // Create chart
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'BMI Categories',
                data: data,
                backgroundColor: backgroundColors,
                borderColor: colors,
                borderWidth: 1
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
                        afterLabel: function(context) {
                            if (context.dataIndex === userIndex) {
                                return `Your BMI: ${userBMI}`;
                            }
                            return '';
                        }
                    }
                },
                annotation: {
                    annotations: {
                        line1: {
                            type: 'line',
                            yMin: userBMI,
                            yMax: userBMI,
                            borderColor: 'black',
                            borderWidth: 2,
                            label: {
                                content: `Your BMI: ${userBMI}`,
                                enabled: true
                            }
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    min: 15,
                    max: 40,
                    title: {
                        display: true,
                        text: 'BMI Value'
                    }
                }
            }
        }
    });
}

/**
 * Macro nutrients pie chart
 */
function initMacroChart() {
    const ctx = document.getElementById('macroChart').getContext('2d');
    const proteinGrams = parseInt(document.getElementById('macroChart').dataset.protein);
    const fatGrams = parseInt(document.getElementById('macroChart').dataset.fat);
    const carbGrams = parseInt(document.getElementById('macroChart').dataset.carbs);
    
    // Calculate calories from each macro
    const proteinCals = proteinGrams * 4;
    const fatCals = fatGrams * 9;
    const carbCals = carbGrams * 4;
    
    // Create pie chart
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Protein', 'Fat', 'Carbs'],
            datasets: [{
                data: [proteinCals, fatCals, carbCals],
                backgroundColor: [
                    '#2286c3', // Blue for protein
                    '#519657', // Green for fat
                    '#fff59d'  // Yellow for carbs
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label;
                            const value = context.raw;
                            const total = context.dataset.data.reduce((acc, val) => acc + val, 0);
                            const percentage = Math.round((value / total) * 100);
                            return `${label}: ${percentage}% (${value} calories)`;
                        },
                        afterLabel: function(context) {
                            const label = context.label;
                            if (label === 'Protein') {
                                return `${proteinGrams}g`;
                            } else if (label === 'Fat') {
                                return `${fatGrams}g`;
                            } else if (label === 'Carbs') {
                                return `${carbGrams}g`;
                            }
                            return '';
                        }
                    }
                }
            }
        }
    });
}