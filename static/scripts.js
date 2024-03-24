function ajouterParticipant() {
    var prenom = $("input[name='prenom']").val();
    var nom = $("input[name='nom']").val();
    var email = $("input[name='email']").val();

    $.post("/ajouter_p", { prenom: prenom, nom: nom, email: email }, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            $("input[name='prenom']").val('');
            $("input[name='nom']").val('');

            // Rafraîchir la page après une action réussie
            location.reload();
        }
    });
}

function supprimerParticipant() {
    var selectedParticipantId = $("select[name='participants']").val();

    $.post("/supprimer_p/" + selectedParticipantId, {}, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            location.reload();
        }
    });
}

function modifierValeur() {
    var selectedParticipantId = $("select[name='participants']").val();
    var nouvelleValeur = $("input[name='nouvelleValeur']").val();

    $.post("/modifier/" + selectedParticipantId, { nouvelleValeur: nouvelleValeur }, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            location.reload();
        }
    });
}

function ajouterMot() {
    var mot = $("input[name='mot']").val();
    var prix = $("input[name='prix']").val();

    $.post("/ajouter_m", { mot: mot, prix: prix }, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            $("input[name='mot']").val('');
            $("input[name='prix']").val('');

            // Rafraîchir la page après une action réussie
            location.reload();
        }
    });
}

function supprimerMot() {
    var selectedMotId = $("select[name='mot']").val();

    $.post("/supprimer_m/" + selectedMotId, {}, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            location.reload();
        }
    });
}

function authentifierUtilisateur() {
    var utilisateur = $("input[name='utilisateur']").val();
    var mdp = $("input[name='mdp']").val();

    $.post("/authentification", { utilisateur: utilisateur, mdp: mdp }, function (response) {
        alertMessage(response.message, response.type);
        if (response.type === 'success') {
            // L'authentification a réussi, définissez la variable authenticated à true.
            authenticated = true;

            // Fermez le modal et affichez le menu.
            var modal_cp = document.getElementById("ajoutModal_cp");
            modal_cp.style.display = "none";
            toggleMenu();
        }
    });

    // Empêche le formulaire de soumettre la page (comportement par défaut).
    return false;
}

function toggleMenu() {
    var menu = document.getElementById("menu");
    var modal_cp = document.getElementById("ajoutModal_cp");

    // Vérifiez si l'utilisateur est authentifié.
    if (authenticated) {
        menu.style.display = (menu.style.display === 'none' || menu.style.display === '') ? 'block' : 'none';
    } else {
        // Si l'utilisateur n'est pas authentifié, ouvrez le modal de connexion.
        modal_cp.style.display = "block";
    }
}

function alertMessage(message, type) {
    alert(message);
}

function openModal_ap() {
    var modal = document.getElementById("ajoutModal_ap");
    modal.style.display = "block";
}

function closeModal_ap() {
    var modal = document.getElementById("ajoutModal_ap");
    modal.style.display = "none";
}

function openModal_sp() {
    var modal = document.getElementById("ajoutModal_sp");
    modal.style.display = "block";
}

function closeModal_sp() {
    var modal = document.getElementById("ajoutModal_sp");
    modal.style.display = "none";
}

function openModal_ma() {
    var modal = document.getElementById("ajoutModal_ma");
    modal.style.display = "block";
}

function closeModal_ma() {
    var modal = document.getElementById("ajoutModal_ma");
    modal.style.display = "none";
}

function openModal_am() {
    var modal = document.getElementById("ajoutModal_am");
    modal.style.display = "block";
}

function closeModal_am() {
    var modal = document.getElementById("ajoutModal_am");
    modal.style.display = "none";
}

function openModal_sm() {
    var modal = document.getElementById("ajoutModal_sm");
    modal.style.display = "block";
}

function closeModal_sm() {
    var modal = document.getElementById("ajoutModal_sm");
    modal.style.display = "none";
}

function openModal_cp() {
    var modal = document.getElementById("ajoutModal_cp");
    modal.style.display = "block";
}

function closeModal_cp() {
    var modal = document.getElementById("ajoutModal_cp");
    modal.style.display = "none";
}