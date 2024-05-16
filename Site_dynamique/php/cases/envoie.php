<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
</html>
<?php
// Connexion à la base de données
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "builder";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Configuration pour lever des exceptions en cas d'erreur
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Création ou mise à jour des données dans la base de données
if($_SERVER["REQUEST_METHOD"] == "POST") {
    // Vérifier si toutes les cases existent déjà dans la base de données
    $check_sql = "SELECT COUNT(*) as count FROM Cases";
    $check_stmt = $conn->prepare($check_sql);
    $check_stmt->execute();
    $row = $check_stmt->fetch(PDO::FETCH_ASSOC);

    if ($row['count'] == 0) {
        // Si aucune case n'existe, créer toutes les cases
²        for ($i = 0; $i < 32; $i++) {
            $type_case = $_POST["type$i"];
            $nom = $_POST["nom$i"];
            $prix = $_POST["prix$i"];
            $loyer = $_POST["loyer$i"];
            $resource_contenue = $_POST["resource$i"];

            // Insérer un nouvel enregistrement
            $insert_sql = "INSERT INTO Cases (type_case, nom, prix, loyer, resource_contenue) 
                    VALUES (:type_case, :nom, :prix, :loyer, :resource_contenue)";
            $stmt = $conn->prepare($insert_sql);
            $stmt->bindParam(':type_case', $type_case);
            $stmt->bindParam(':nom', $nom);
            $stmt->bindParam(':prix', $prix);
            $stmt->bindParam(':loyer', $loyer);
            $stmt->bindParam(':resource_contenue', $resource_contenue);
            $stmt->execute();
        }
        echo "Toutes les cases ont été créées avec succès.";
    } else {
        // Si des cases existent déjà, mettre à jour les enregistrements si nécessaire
        for ($i = 0; $i < 32; $i++) {
            $type_case = $_POST["type$i"];
            $nom = $_POST["nom$i"];
            $prix = $_POST["prix$i"];
            $loyer = $_POST["loyer$i"];
            $resource_contenue = $_POST["resource$i"];
            
            // Mettre à jour l'enregistrement existant
            $update_sql = "UPDATE Cases SET nom = :nom, prix = :prix, loyer = :loyer, resource_contenue = :resource_contenue, type_case = :type_case WHERE id_Cases = :id_Cases";
            $stmt = $conn->prepare($update_sql);
            $stmt->bindParam(':nom', $nom);
            $stmt->bindParam(':prix', $prix);
            $stmt->bindParam(':loyer', $loyer);
            $stmt->bindParam(':resource_contenue', $resource_contenue);
            $stmt->bindParam(':type_case', $type_case);
            $id_case = $i + 1;
            $stmt->bindParam(':id_Cases', $id_case);
            $stmt->execute();
        }
        echo "Les données ont été mises à jour avec succès.";
    }
}
?>
