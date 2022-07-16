 We can create docker instance of our ImageClasssification model Using model_serve.sh command 
 
 sudo docker run -p 8501:8501 --name=pets -v "/home/rhyme/Desktop/app/pets/:/models/pets/1" -e MODEL_NAME=pets -t tensorflow/serving
 
```
  
  specifying the tensorflow serving port ->   -p 8501:8501
  
  
  docker instance name -> --name=pets
  
  
  This argument tells the path of the model ->  /home/rhyme/Desktop/app/pets/

  this is to specify the path where our saved model is to be saved in our docker instance where we have to copy the model with the version i.e in this case is 1 -> /models/pets/1
  Here model is the directory and /pets is anything but it should match with our MODEL_NAME env variable which we have set in this docker model instance
 


```
