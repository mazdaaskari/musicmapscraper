## Music Map Scraper
### From : Mazda Askari 
##### mazdaaskari@outlook.com
###### All data displayed by this program is received from [Music Map](https://www.music-map.com)

With the help of this app, 
you can find music that suits your taste 
by entering the name of your favorite singer or band.

To use this program, first install libraries in requirements.txt, with the help of this command: 
```
pip install requirements.txt
```
and enter your favorite artist/band name like this : 
```
python main.py --artistname 'artist name'
```
  or
```
python main.py --artistname artistname
```
  or
```
python main.py -a 'artist name'
```  
or
```
python main.py -a artistname
```  
Example :
```
python main.py --artistname 'pink floyd'
```
  or
```
python main.py --artistname metallica
```
  or
```
python main.py -a 'linkin park'
```  
or
```
python main.py -a eminem
```    

- *Important : Be sure to use  ```' ' ``` for two-word artist/band names or more*

**if you want to output the artists/bands in a text file use the``` --output ``` option.**
**if you don't use the file path after this command, the file will be created in the current path of the program.**
Example :
```
python main.py --artistname 'pink floyd' --output 
```
```
python main.py --artistname 'pink floyd' --output  /home/
```


**Thank You All**
