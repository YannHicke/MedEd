from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Load and process the JSON data
with open('../results/context_GI_Bleeding_2024-03-28_13-06-16_results.json', 'r') as file:
    data = json.load(file)

# HTML template with embedded Python (Jinja2) for dynamic content
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>GI Bleeding Analysis Dashboard</title>
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
        color: #333;
    }
    h1 {
        color: #333;
        text-align: center;
        margin-top: 0;
    }
    .category {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 20px;
        margin-bottom: 30px;
    }
    .category-title {
        color: #007bff;
        border-bottom: 2px solid #eeeeee;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .item {
        background-color: #f9f9f9;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 5px;
        transition: transform 0.3s ease-in-out;
    }
    .item:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 20px;
        color: #0056b3;
        margin: 0;
    }
    .discussed {
        font-size: 16px;
        color: #28a745;
        margin-top: 5px;
    }
    .explanation {
        margin-top: 10px;
        font-size: 14px;
        text-align: justify;
    }
</style>

</head>
<body>
    <h1>OSCE James Turner - GI Bleeding<br>Student Niroop Rajashekar</h1>
    {% for category_name, category_items in data.items() %}
        <div class="category">
            <h2 class="category-title">{{ category_name.replace('_', ' ') }}</h2>
            {% for item_name, item_details in category_items.items() %}
                <div class="item">
                    <div class="title">{{ item_name.replace('_', ' ') }}</div>
                    <div class="discussed">Discussed: {{ item_details["discussed"] }}</div>
                    <div class="explanation">{{ item_details["explanation"] }}</div>
                </div>
            {% endfor %}
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, data=data)

if __name__ == '__main__':
    app.run(debug=True)
