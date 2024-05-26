<!-- 
qui: Nathan
quoi: gestionnaire des cart chance (interface et lecture de la db)
quand: 
- 17/05/2024 Nathan
- 18/05/2024 Nathan
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

// Récupération des cartes chance depuis la base de données
$sql = "SELECT * FROM CarteChance";
$result = $conn->query($sql);

?>

<!--Création du HTML-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cartes Chance</title>
</head>
<body>
    <h1>Cartes Chance</h1>
    <h2>Liste Carte chance existantes :</h2>
    <?php
    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "<p>Titre: " . $row["titre"]. " - contennu: " . $row["contennu"]. "</p>";
        }
    } else {
        echo "<p>Aucune carte chance trouvée.</p>";
    }
    ?>
    <h2>Nouvelle carte chance :</h2>
    <form method="post" action="envoie.php">
        Titre: <input type="text" name="titre"><br>
        contennu: <textarea name="contennu"></textarea><br>
        Action (veuiller entrer du code python): 
        
        <textarea type="text" name="action">
        Ex: print("Vous avez mangé le joueur ayant jouer juste avant vous mouhahaha. Il ne peu donc plus jouer, dommage.")
        precedent = listeJoueurs[listeJoueurs.index(jActif) - 1]
        listeJoueurs.pop(precedent);
        ---
        Ex2: print("Vous avez perdu 250")
        jActif.argent -= 250'
        </textarea>
        
        <input type="submit" value="Créer">
    </form>
</body>
</html>

<?php
$conn->close();
?>
