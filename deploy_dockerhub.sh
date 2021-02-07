docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
TAG="latest"
else
TAG="$TRAVIS_BRANCH"
fi
#docker build -f Dockerfile -t $TRAVIS_REPO_SLUG:$TAG .
docker build -f Dockerfile -t $DOCKER_REPO .
sudo docker tag $DOCKER_REPO $DOCKER_REPOM
sudo docker push $DOCKER_REPO:$TAG
