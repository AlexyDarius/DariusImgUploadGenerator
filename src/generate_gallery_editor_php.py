def generate_gallery_editor_php(directory_path, main_domain, full_body_tag):
    php_code = f'''<?php
include "https://{main_domain}/includes/head.php"
?>

    <title>Votre interface de gestion de galerie</title>
    <link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/gallery/css/style.css">
</head>
{full_body_tag}
<?php

require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php';
require $_SERVER['DOCUMENT_ROOT']. '/modules/gallery/requires/upload_image.php';

?>

<?php
include "https://{main_domain}/includes/navbar.php"
?>

    <header>
        <h1 style="margin: 32px; font-weight: bold; text-align: center">Bienvenue sur votre espace gestionnaire de galerie</h1>
    </header>

    <!-- Form for uploading images -->
    <div id="upload-container">
        <form id="image-upload-form" method="post" enctype="multipart/form-data" onsubmit="uploadImage(event);">
            <label for="image">Sélectionnez une image à télécharger (100ko max, utiliser <a href="https://cloudconvert.com/webp-converter">compression webp</a>, taille max conseillée 512x512px):</label>
            <input type="file" name="image" id="image" accept="image/*" required>
            <input type="hidden" name="MAX_FILE_SIZE" value="100000"> <!-- 100ko -->
            <label for="legend">Légende (255 caractères max):</label>
            <input type="text" name="legend" id="legend" required maxlength="255">
            <button type="submit">Envoyer l'image</button>
            <label for="warning">! Ne pas cliquer plusieurs fois sur le bouton d'envoi !</label>
            <div id="error-message" style="color: red; display: none;"></div>
        </form>
        <div id="status-message"></div>
    </div>

    <div id="image-container">

<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/gallery/requires/back_office_display.php';
?>

</div>
    <p style="text-align: center; font-size: 24px"><a href="index.php">Revenir à l'accueil</a></p>
</div>

    <script src="js/script.js"></script>
    <script src="js/uploadImage.js"></script>

<?php
include "https://{main_domain}/includes/footer.php"
?>

'''

    with open(f"{directory_path}/gallery/gallery-editor.php", "w") as php_file:
        php_file.write(php_code)
