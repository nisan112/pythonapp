<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Official Daily Blog Django App</title>
</head>
<body>

<h1>Official Daily Blog Django App</h1>

<p>This is the official Daily Blog Django app, which provides a platform for users to write, manage, and share daily blogs. It comes with authentication features like registration, login, and logout, implemented using Django's built-in authentication system.</p>

<h2>Authentication Features</h2>
<p>Users can log in as a regular user or as an admin. Below are the steps to set up and run the app:</p>

<h3>Setting Up the Environment</h3>
<ul>
    <li>Ensure that you have the latest version of Python installed.</li>
    <li>Create a virtual environment by running:
        <pre><code>python -m venv venv</code></pre>
    </li>
    <li>Activate the virtual environment:
        <pre><code>source venv/bin/activate  <!-- For Mac/Linux -->
        venv\Scripts\activate  <!-- For Windows --></code></pre>
    </li>
    <li>Install Django within the virtual environment:
        <pre><code>pip install django</code></pre>
    </li>
</ul>

<h3>Creating Superuser</h3>
<p>To access the admin panel, you need to create a superuser account. Run the following command in the terminal:</p>
<pre><code>python manage.py createsuperuser</code></pre>
<p>Enter the necessary credentials (username, email, password) when prompted.</p>

<h3>Running the Server</h3>
<p>To start the development server, run the following command:</p>
<pre><code>python manage.py runserver</code></pre>
<p>Once the server is running, navigate to <strong>http://127.0.0.1:8000/</strong> in your browser to access the app.</p>

<h2>Accessing the Admin Panel</h2>
<p>To log in as an admin, go to <strong>http://127.0.0.1:8000/admin</strong> and enter the superuser credentials you created earlier.</p>

<h3>Features Available</h3>
<ul>
    <li>Blog Creation and Management: Create, edit, and delete blogs as a user.</li>
    <li>User Authentication: Login, logout, and register new users.</li>
    <li>Admin Dashboard: Manage user accounts and blog posts as an admin.</li>
</ul>

<h2>Project Structure</h2>
<p>The project follows the typical Django app structure. Below is the directory structure for this project:</p>
<ul>
    <li><strong>manage.py</strong>: Command-line utility for managing the project.</li>
    <li><strong>pythonapp/</strong>: The main project folder containing the settings and configuration files.
        <ul>
            <li><strong>pythonapp/settings.py</strong>: Django settings, including database configuration and installed apps.</li>
            <li><strong>pythonapp/urls.py</strong>: URL routing for the entire project.</li>
            <li><strong>pythonapp/wsgi.py</strong>: WSGI entry point for deploying the app to production.</li>
        </ul>
    </li>
    <li><strong>index/</strong>: The Django app for the index page and other functionality.
        <ul>
            <li><strong>index/models.py</strong>: Defines the database models for the index app.</li>
            <li><strong>index/views.py</strong>: Contains the views that handle the app's logic for the index page.</li>
            <li><strong>index/urls.py</strong>: App-specific URL routing for the index app.</li>
            <li><strong>index/templates/</strong>: HTML templates for rendering the index page and other related pages.</li>
        </ul>
    </li>
    <li><strong>db.sqlite3</strong>: Default SQLite database file (you can switch to PostgreSQL or MySQL for production).</li>
</ul>

<h3>Contributing</h3>
<p>If you'd like to contribute to the development of this project, feel free to fork the repository, make your changes, and submit a pull request.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>

