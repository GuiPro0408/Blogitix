<!DOCTYPE html>
<html>
  <head>
    <title>Technical Specification for Basic Blog Application</title>
  </head>
  <body>
    <h1>Overview</h1>
    <p>The Basic Blog Application is a simple blog website that allows users to create, view, edit, and delete blog posts. Users can also add categories to their posts and search for blog posts.</p>
    <h2>Technologies</h2>
    <ul>
      <li>Python</li>
      <li>Django</li>
      <li>HTML5</li>
      <li>CSS3</li>
      <li>SQLite3 (default database)</li>
    </ul>
    <h2>Functional Requirements</h2>
    <ol>
      <li>User Registration: Users should be able to register for an account by providing their email, username, and password.</li>
      <li>User Authentication: Users should be able to log in and log out of their account.</li>
      <li>Create Blog Posts: Users should be able to create new blog posts by providing a title, content, and category (optional).</li>
      <li>Edit Blog Posts: Users should be able to edit existing blog posts.</li>
      <li>Delete Blog Posts: Users should be able to delete their own blog posts.</li>
      <li>View Blog Posts: Users should be able to view a list of all blog posts and view the details of a specific blog post.</li>
    </ol>
    <h2>Database Schema</h2>
    <p>The Basic Blog Application will use three models:</p>
    <ul>
      <li>User: This model will be used to store user information such as username, email, and password.</li>
      <li>Post: This model will be used to store blog post information such as title, content, author (foreign key to User), category (optional), created date, and modified date.</li>
      <li>Category: This model will be used to store category information such as name and description.</li>
    </ul>
  </body>
</html>
