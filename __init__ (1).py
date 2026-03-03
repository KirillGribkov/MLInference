<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            Predicting_employee_dismisal
        </title>
    </head>
    <body>
        <h1>Predicting employee dismisal</h1>
        <form action="" method="post">
            {% csrf_token %}
            {{form}}
            <input type="submit" value="Submit">
        </form>
        {% if otvet %}
            <h3>Otvet: {{otvet}}</h3>
        {% else %}
            <h3>Otveta poka net</h3>
        
        {% endif %}
        {% if model %}
            <h3>Model: {{model}}</h3>
        {% endif %}
        <h2>ШИФТ</h2>
        <h3>Трек: Класический ml</h2>
    </body>
</html>