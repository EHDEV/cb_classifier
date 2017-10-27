## Clickbait Classifier API

#### Docker Version: 17.09.0
  
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

_Check if api is up and working_
``` GET http://localhost:5000 ```

_Train model_
``` GET http://localhost:5000/train ```

_Get model classification report on default train/test_
``` GET http://localhost:5000/classification_report ```

_Predict Clickbait probability of a title._

``` POST http://localhost:5000/clickbait_predict  ```

with a json body similar to the schemas below
```
{"title": "title of article to be predicted"} or 
[{"title": "title of article to be predicted"}, {"title": "title of article to be predicted"}]

```

