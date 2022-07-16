### sudo docker run -p 8501:8501 --name=pets -v "/home/rhyme/Desktop/app/pets/:/models/pets/1" -e MODEL_NAME=pets -t tensorflow/serving
```

```
* This argument tells the path of the model - /home/rhyme/Desktop/app/pets/

```
```
this is to specify the path in our deocker instance where we have to copy the model with the verion i.e in this case is 1 - /models/pets/1
```


```
