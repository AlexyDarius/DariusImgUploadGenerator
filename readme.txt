Add the "gallery" folder into your DariusDev modules folder
Add the "gallery.php" file at the website html root

Make sure you have a database "{website}_db" in your databases
Create the table for the gallery inside the database: 

CREATE TABLE `{website}_gallery` (
  `id` int(11) NOT NULL,
  `filename` varchar(255) NOT NULL,
  `uploaded_by` varchar(255) NOT NULL,
  `legend` varchar(255) NOT NULL,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


**Add your db key at the beginning of db name