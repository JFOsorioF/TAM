# Juan Felipe Osorio Franco

## Como Correr

Elegi utilizar torch para entrenar la red dado que es lo que mejor conozco, me base en varios codigos existentes. El proyecto quedo estructurado de la siguiente manera:

- Para entrenar el modelo, correr `train.ipynb` en Colab. Deberia funcionar ssin problemas.
- Para ver los resultados del modelo se debe bajar archivo `.chkpt` que se crea al terminar el entrenamiento (O al interrumpirlo) y ponerlo en la carpeta `checkpoints`. Se puede usar tambien el checkpoint ya entrenado que adjunto en la carpeta, en tal caso ignorar el siguiente paso.
- En `play.py` buscar la linea `checkpoint = torch.load(str(save_dir / 'mario_net_3.chkpt'))` Y cambiar el nombre del checkpoint adecuadamente.
- Intalar el ambiente de conda descrito en `enviroment.tml` con el comando `conda env create -f enviroment.yml` y activarlo con `conda activate mario`
- Ubicarse en la carpeta Mario (`cd Corte3/Mario`) y correr el modelo con `python play.py`

Si no funciona adjunto un video de la red jugando.
