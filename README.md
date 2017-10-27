## Clickbait Classifier API

### Docker Version: 
  `__Docker version 17.09.0__`
  
To build the container:
 - clone this repository
 - build the docker image run the following in your terminal
 ```
 docker build -t cb_classifier . 
```
 - Run the container once the build is complete
```
docker run -p 5000:5000 cb_classifier 
```

Once the container is up and running access the api as follows:

#### Check if api is up and working 
``` GET http://localhost:5000 ```

#### Train model
``` GET http://localhost:5000/train ```

#### Get model classification report on default train/test 
``` GET http://localhost:5000/classification_report ```

#### Predict Clickbait probability of a title. 

``` POST http://localhost:5000/clickbait_predict  ```

with a json body with a similar schemas as below

```
{"title": "title of article to be predicted"} or 
[{"title": "title of article to be predicted"}, {"title": "title of article to be predicted"}]

```

