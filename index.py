<!DOCTYPE html>
<html>
<head>
  <title>ATS Resume Generator</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <h1>📄 Free ATS Resume Generator</h1>
  <form action="/generate" method="POST">
    <input type="text" name="name" placeholder="Full Name" required><br>
    <textarea name="summary" placeholder="Professional Summary" required></textarea><br>
    <button type="submit">Generate Resume PDF</button>
  </form>
</body>
</html>
