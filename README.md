# 🍔 Exploratory Data Analysis (EDA) - McDonald's Nutritional Data

## 📌 Objective
This project aims to analyze the **nutritional values of McDonald's food items** to understand trends in calorie intake, fat content, sodium levels, and correlations between nutrients. The insights from this analysis can help customers make informed dietary choices and assist McDonald's in optimizing its menu offerings.

## 📊 Dataset Overview
The dataset contains details about various **McDonald's food items** and their **nutritional values**. The key columns in the dataset include:

- **Category**: The type of food item (e.g., Burgers, Coffee & Tea, Salads, etc.)
- **Item**: The specific name of the food item
- **Serving Size**: The portion size of the food item
- **Calories**: Total energy content
- **Calories from Fat**: Energy derived from fat content
- **Total Fat**: Amount of fat in grams
- **Total Fat (% Daily Value)**: Percentage of daily recommended fat intake
- **Saturated Fat**: Amount of saturated fat in grams
- **Saturated Fat (% Daily Value)**: Percentage of daily recommended saturated fat intake
- **Trans Fat**: Amount of trans fat in grams
- **Cholesterol**: Cholesterol content in mg
- **Cholesterol (% Daily Value)**: Percentage of daily recommended cholesterol intake
- **Sodium**: Amount of sodium in milligrams
- **Sodium (% Daily Value)**: Percentage of daily recommended sodium intake
- **Carbohydrates**: Total carbohydrate content in grams
- **Carbohydrates (% Daily Value)**: Percentage of daily recommended carbohydrate intake
- **Dietary Fiber**: Amount of fiber in grams
- **Dietary Fiber (% Daily Value)**: Percentage of daily recommended fiber intake
- **Sugars**: Total sugar content in grams
- **Protein**: Amount of protein in grams
- **Vitamin A (% Daily Value)**: Percentage of daily recommended Vitamin A intake
- **Vitamin C (% Daily Value)**: Percentage of daily recommended Vitamin C intake
- **Calcium (% Daily Value)**: Percentage of daily recommended Calcium intake
- **Iron (% Daily Value)**: Percentage of daily recommended Iron intake

## 🔍 Key Analyses Performed

### 1️⃣ **Food Categories Analysis**
- **Highest variety**: Coffee & Tea
- **Lowest variety**: Salads

### 2️⃣ **Outlier Detection**
- **Columns with outliers**: `Calories`, `Calories from Fat`, `Total Fat`
- **Columns without outliers**: `Saturated Fat`

### 3️⃣ **Correlation Analysis**
Identified **strong correlations** between key nutritional variables:

**With Calories:**
- Calories & Iron **(0.64)**
- Calories & Sodium **(0.71)**
- Calories & Cholesterol **(0.68)**
- Calories & Saturated Fat **(0.85)**

**With Total Fat:**
- Total Fat & Iron **(0.73)**
- Total Fat & Protein **(0.81)**
- Total Fat & Dietary Fiber **(0.58)**
- Total Fat & Sodium **(0.85)**
- Total Fat & Cholesterol **(0.68)**
- Total Fat & Saturated Fat **(0.85)**

(Additional correlation lists available in the dataset analysis.)

### 4️⃣ **Cholesterol Analysis**
- **Category contributing most to cholesterol intake**: **Breakfast**

### 5️⃣ **Sodium Content Analysis**
- **Food item with the highest sodium intake**: **Chicken McNuggets**

### 6️⃣ **Saturated Fat Content Analysis**
- **Top 4 food items with the highest saturated fat:**
  - McFlurry with M&M’s Candies (Medium)
  - Big Breakfast with Hotcakes (Large Biscuit)
  - Chicken McNuggets (40 piece)
  - Frappé Chocolate Chip (Large)

## 📈 Visualizations
- **Bar Plots**: Show distribution of food categories, sodium levels, and cholesterol content.
- **Box Plots**: Detect outliers in calories, fat, and sodium levels.
- **Heatmaps**: Display correlations between various nutritional values.

## 🏆 Conclusion
- **Coffee & Tea have the most varieties**, whereas **Salads have the least**.
- **Calories, Fat, and Sodium show strong correlations** with other nutrients.
- **Breakfast items contribute the most to cholesterol intake**.
- **Chicken McNuggets contain the highest sodium levels**.
- **McFlurry, Big Breakfast, and Frappé have the highest saturated fat content**.

