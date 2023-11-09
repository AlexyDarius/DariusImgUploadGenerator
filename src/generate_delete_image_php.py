def generate_delete_image_php(directory_path, website):
    php_code = f'''<?php

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['image_id'])) {{
    // Retrieve the image ID from the POST request
    $imageId = $_POST['image_id'];

    // Connect to the MySQL database
    $conn = new mysqli("localhost", $_SERVER['DB_{website}_USERNAME'], $_SERVER['DB_{website}_PASSWORD'], $_SERVER['DB_{website}_DB']);
    if ($conn->connect_error) {{
        die("Connection failed: " . $conn->connect_error);
    }}

    // Retrieve the image filename from the database
    $sql = "SELECT filename FROM {website}_gallery WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $imageId);
    $stmt->execute();
    $stmt->bind_result($imageFilename);
    $stmt->fetch();
    $stmt->close();

    if (!empty($imageFilename)) {{
        // Delete the image file from the server
        $imagePath = "../images/" . $imageFilename;
        if (file_exists($imagePath)) {{
            unlink($imagePath);
        }}

        // Delete the database entry
        $sql = "DELETE FROM {website}_gallery WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $imageId);
        $stmt->execute();
        $stmt->close();

        echo "Image supprimée !";
    }} else {{
        echo "Image impossible à trouver.";
    }}

    $conn->close();
}}

?>

'''

    with open(f"{directory_path}/gallery/requires/delete_image.php", "w") as php_file:
        php_file.write(php_code)
        print("delete_image.php generated !")
