<!--Connexion à la db-->

<?php
// Connexion à la base de données
$conn = new mysqli("localhost", "root", "root", "builder");

// Vérification de la connexion
if ($conn->connect_error) {
    die("Connexion échouée: " . $conn->connect_error);
}

// Traitement des données envoyées par le formulaire
for ($i = 0; $i < 32; $i++) {
    $type_case = $_POST["type_case$i"];
    $nom = $_POST["nom$i"];
    $prix = $_POST["prix$i"];
    $loyer = $_POST["loyer$i"];
    $resource = $_POST["resource$i"];
    $nbr_ressource = $_POST["Nbr_ressource$i"];

    // Exemple de requête SQL d'insertion
    $sql = "INSERT INTO Cases (type_case, nom, prix, loyer, resource_contenue, nbr_ressource) VALUES ('$type', '$nom', '$prix', '$loyer', '$resource', '$nbr_ressource')";
    
    // Exécution de la requête SQL
    if ($conn->query($sql) === TRUE) {
        echo "Nouvel enregistrement créé avec succès";
    } else {
        echo "Erreur: " . $sql . "<br>" . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gestion des cases</title>

<!--CSS-->

<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    #board {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        padding: 20px;
    }
    .case {
        width: 200px;
        height: 200px;
        background-color: #eee;
        border: 1px solid #ccc;
        border-radius: 5px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 10px;
    }
    .case select, .case input {
        width: 80%;
        margin-top: 5px;
    }
    .hidden {
        display: none;
    }
</style>
</head>
<body>

<div id="board">
    <?php for ($i = 0; $i < 32; $i++): ?>
        <div class="case">
            <div>
                <label for="type<?php echo $i; ?>">Type:</label>
                <select class="case-type" id="type<?php echo $i; ?>">
                    <option value="case">Case</option>
                    <option value="case_propriete">Case Propriete</option>
                    <option value="case_ressource">Case Ressource</option>
                    <option value="case_vol">Case Vol</option>
                    <option value="case_chance">Case Chance</option>
                    <option value="case_police">Case Police</option>
                </select>
            </div>
            <div class="nom hidden">
                <label for="nom<?php echo $i; ?>">Nom:</label>
                <input type="text" id="nom<?php echo $i; ?>" name="nom<?php echo $i; ?>">
            </div>

            <div class="prix hidden">
                <label for="prix<?php echo $i; ?>">Prix:</label>
                <input type="text" id="prix<?php echo $i; ?>" name="prix<?php echo $i; ?>">
            </div>
            <div class="loyer hidden">
                <label for="loyer<?php echo $i; ?>">Loyer:</label>
                <input type="text" id="loyer<?php echo $i; ?>" name="loyer<?php echo $i; ?>">
            </div>
            <div class="resource hidden">
                <label for="resource<?php echo $i; ?>">Resource Contenue:</label>
                <input type="text" id="resource<?php echo $i; ?>" name="resource<?php echo $i; ?>">
            </div>
            <div class="Nbr_ressource hidden">
                <label for="Nbr_ressource<?php echo $i; ?>"> Nombre de ressources:</label>
                <input type="text" id="Nbr_ressource<?php echo $i; ?>" name="Nbr_ressource<?php echo $i; ?>">
            </div>
            <div class="case-number">Case <?php echo $i; ?></div>
        </div>
    <?php endfor; ?>
</div>

<script>
const caseTypes = document.querySelectorAll('.case-type');
caseTypes.forEach(select => {
    select.addEventListener('change', function() {
        const selectedOption = this.value;
        const caseDiv = this.closest('.case');

        const textFields = caseDiv.querySelectorAll('.nom, .prix, .loyer, .resource, .Nbr_ressource');
        textFields.forEach(field => field.classList.add('hidden'));

        switch(selectedOption) {
            
            case 'case_propriete':
                caseDiv.querySelector('.nom').classList.remove('hidden');
                caseDiv.querySelector('.prix').classList.remove('hidden');
                caseDiv.querySelector('.loyer').classList.remove('hidden');
                break;
            
            case 'case_ressource':
                caseDiv.querySelector('.resource').classList.remove('hidden');
                break;

            case 'case_vol':
                caseDiv.querySelector('.Nbr_ressource').classList.remove('hidden')
                break;
            
            default:
                break;
        }
    });
});

window.addEventListener('DOMContentLoaded', function() {
    const allTextFields = document.querySelectorAll('.nom, .prix, .loyer, .resource');
    allTextFields.forEach(field => field.classList.add('hidden'));
});
</script>