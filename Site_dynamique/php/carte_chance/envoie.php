<-- 
qui: Nathan
quoi: gestionnaire d'envoie  a la db les cartes chances
quand: 
- 17/05/2024 Nathan
-->
<?php
// Connexion à la base de données
$servername = "localhost";
$username = "root";
$password = "root";
$database = "Builder";

$conn = new mysqli($servername, $username, $password, $database);


// Vérification de la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Si le formulaire est soumis, insérer une nouvelle carte chance
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $titre = $_POST["titre"];
    $contennu = $_POST["contennu"];
    $action = $_POST["action"];

    $sql = "INSERT INTO CarteChance (titre, contennu, action) VALUES ('$titre', '$contennu', '$action')";
    
    if ($conn->query($sql) === TRUE) {
        echo "Nouvelle carte chance créée avec succès !";
    } else {
        echo "Erreur: " . $sql . "<br>" . $conn->error;
    }
}