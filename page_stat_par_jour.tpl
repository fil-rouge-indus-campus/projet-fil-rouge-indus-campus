<h1>Ceci est la page des statistiques par jour qui reçoit en parametre la machine {{nom}}</h1>
% for item in stats:
   {{item.machine}}
   {{item.nb_partie_jour}}
   {{item.duree_moy_partie_jour}}
   {{item.nb_fois_gagnant1}}
   {{item.nb_fois_gagnant2}}
   {{item.nb_fois_egalite}}

   <br>

% end