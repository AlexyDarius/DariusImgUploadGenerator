def generate_bo_display_php(directory_path, website):
    php_code = f'''<?php
// Connect to the MySQL database (adjust the connection details as per your configuration)
$conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
if ($conn->connect_error) {{
    die("Connection failed: " . $conn->connect_error);
}}

// Retrieve image information from the database
$sql = "SELECT filename, legend, id FROM {website}_gallery ORDER BY upload_date DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {{
    while ($row = $result->fetch_assoc()) {{
        $imagePath = "images/" . $row['filename'];
        $imageId = $row['id'];
        $legend = $row['legend'];
        
        echo "<div class='image-box'>";
        echo "<img src='$imagePath' alt='Image'>";
        echo "<p id='legend-$imageId'>$legend</p>";
        echo "<button class='delete-button' data-image-id='$imageId'>Supprimer</button>";
        echo " <button class='edit-button' data-image-id='$imageId'>Éditer</button>";

        echo "<div class='edit-container' id='edit-container-$imageId' style='display: none;'>";
        echo "<input type='text' id='edited-legend-$imageId' placeholder='Éditer la légende'>";
        echo "<button class='save-button' style='margin-right:6px' id='save-button-$imageId' data-image-id='$imageId'>Sauvergarder</button>";
        echo "<button class='cancel-button' id='cancel-button-$imageId' data-image-id='$imageId'>Annuler</button>";
        echo "</div>";

        echo "</div>";
    }}
}} else {{
    echo "No images found.";
}}

$conn->close();
?>
'''

    with open(f"{directory_path}/gallery/requires/back_office_display.php", "w") as php_file:
        php_file.write(php_code)
        print("back_office_display.php generated !")
