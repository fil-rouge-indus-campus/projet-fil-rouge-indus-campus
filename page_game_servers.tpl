<!DOCTYPE html>
<html lang="fr">

<head>
   <meta charset="UTF-8">
   <title>Game Servers</title>
</head>
<body>
<h1> Listing des serveurs de jeu </h1>
<p> nom de la machine / ip de la machine / jeu proposé </p>
% for item in Serveurs_info:
    {{item.nom}}
    {{item.adress_ip}}
    {{item.jeu_installe}}
    <br>
% end

</body>
</html>