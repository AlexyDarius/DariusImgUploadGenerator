def generate_gallery_php(directory_path, main_domain, full_body_tag, gallery_title):
    php_code = f'''<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <title>{gallery_title}</title>
    <link rel="stylesheet" type="text/css" href="https://{main_domain}/modules/gallery/css/style.css">
</head>
{full_body_tag}
<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <header>
        <h1 style="color: var(--bs-secondary);font-family: Lato-Black;font-size: 48px; text-align : center; margin : 32px">Notre galerie</h1>
    </header>

    <h2 style="text-align : center; font-family: Lato-Bold;color: var(--bs-primary);font-size: 24px;">Retrouvez-nous en images !</h2>

    <div id="image-container">

<?php
require $_SERVER['DOCUMENT_ROOT']. '/modules/gallery/requires/gallery_displayer.php';
?>

    </div>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/gallery.php", "w") as php_file:
        php_file.write(php_code)
        print("gallery.php generated !")
