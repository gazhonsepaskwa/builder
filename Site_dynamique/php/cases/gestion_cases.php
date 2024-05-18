<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gestion des cases</title>

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

<form method="post" action="envoie.php">
    <div id="board">
        <?php for ($i = 0; $i < 32; $i++): ?>
            <div class="case">
                <div>
                    <label for="type<?php echo $i; ?>">Type:</label>
                    <select class="case-type" id="type<?php echo $i; ?>" name="type<?php echo $i; ?>">
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
                    <select id="resource<?php echo $i; ?>" name="resource<?php echo $i; ?>">
                        <option value="tractopelle">Tractopelle</option>
                        <option value="grue">Grue</option>
                        <option value="camion">Camion</option>
                        <option value="bateau">Bateau</option>
                    </select>
                </div>

                <div class="case-number">Case <?php echo $i; ?></div>
            </div>
        <?php endfor; ?>
    </div>
    <button type="submit">Enregistrer</button>
</form>


<script>
    // afficher les bon champs en fct du choix dans le dropdown
    const caseTypes = document.querySelectorAll('.case-type');
    caseTypes.forEach(select => {
        select.addEventListener('change', function() {
            const selectedOption = this.value;
            const caseDiv = this.parentElement.parentElement;

            // Tout cacher
            const fields = caseDiv.querySelectorAll('.nom, .prix, .loyer, .resource');
            fields.forEach(field => field.classList.add('hidden'));

            // Afficher les nécécaires 
            switch(selectedOption) {
                case 'case':
                case 'case_chance':
                case 'case_vol':
                case 'case_police':
                    break; // plus rien a afficher
                case 'case_propriete':
                    caseDiv.querySelector('.nom').classList.remove('hidden');
                    caseDiv.querySelector('.prix').classList.remove('hidden');
                    caseDiv.querySelector('.loyer').classList.remove('hidden');
                    break;
                case 'case_ressource':
                    caseDiv.querySelector('.resource').classList.remove('hidden');
                    break;
                    
            }
        });
    });
</script>

</body>
</html>
