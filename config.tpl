<h1>CONFIGURATION</h1>

        <form action="/config" method="post">
            adresse_ip : <input type="text"  name='adresse_ip' value = "0.0.0.0" placeholder="xxx.xxx.xxx.xxx" />
            name_server : <input type="text" name='name_server' value = "0" placeholder=""/>
            game  : <input type="text" name='game' value = "0" placeholder=""/>
            Max player delay : <input type="number" name='Max player delay' step="10" value="0" min="0" max="100"/>
            Max coin blink delay: <input type="number" name='Max coin blink delay' step="10" value="0" min="0" max="100" />
            Victory blink delay : <input type="number" name='Victory blink delay' step="10" value="0" min="0" max="100" />
            level : <input type="number" step="1" name='level' value="0" min="0" max="10" />

             player 1 :
            <select name="nom" size="1">
            <option>rouge
            <option>vert
            <option>bleu
            </select>



             player 2 :
            <select name="nom" size="1">
            <option>rouge
            <option>vert
            <option>bleu
            </select>


         <div>
    <button>Envoyer les modif</button>
        </div>
        </form>