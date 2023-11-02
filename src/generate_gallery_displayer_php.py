def generate_gallery_displayer_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT filename, legend FROM {website}_gallery ORDER BY upload_date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $imagePath = "modules/galleryimages/" . $row['filename'];
        $legend = $row['legend'];
        
        echo "<div class='image-box'>";
        echo "<a href='$imagePath' class='image-link'>";
        echo "<img src='$imagePath' alt='$legend'>";
        echo "</a>";
        echo "<p>$legend</p>";
        echo "</div>";
    }}
}} else {{
    echo "Aucune image trouvée.";
}}

$conn->close();
?>
'''

    with open(f"{directory_path}/gallery/requires/gallery_displayer.php", "w") as php_file:
        php_file.write(php_code)
        print("gallery_displayer.php generated !")
