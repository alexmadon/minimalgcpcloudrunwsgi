# minimalgcpcloudrunwsgi

minimal gcp cloud run wsgi 

https://datasciencecampus.github.io/deploy-dash-with-cloud-run/

https://pythonspeed.com/articles/alpine-docker-python/


https://www.docker.com/blog/containerized-python-development-part-1/


docker build -t myimage .


root@hp:/var/lib/docker# systemctl status | grep dock
           │   │ │ └─23487 grep dock
             ├─docker.service
             │ └─1211 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
root@hp:/var/lib/docker# systemctl status docker.service
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2021-03-01 23:11:23 CET; 1 weeks 5 days ago
     Docs: https://docs.docker.com
 Main PID: 1211 (dockerd)
    Tasks: 22
   Memory: 1.1G
   CGroup: /system.slice/docker.service
           └─1211 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

Mar 14 08:44:41 hp dockerd[1211]: time="2021-03-14T08:44:41.939080072+01:00" level=info msg="Layer sha256:2b2f5943461c1bbecc85f02631fb2aca5ed756c828a433e6612d6db805ea5a0c cleaned up"
Mar 14 08:44:42 hp dockerd[1211]: time="2021-03-14T08:44:42.163213688+01:00" level=info msg="Layer sha256:2b2f5943461c1bbecc85f02631fb2aca5ed756c828a433e6612d6db805ea5a0c cleaned up"
Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.




https://stackoverflow.com/questions/24309526/how-to-change-the-docker-image-installation-directory
WARNING: No swap limit support
 Docker Root Dir: /var/lib/docker


/etc/docker/daemon.json do the trick:

```
{
    "data-root": "/home/madon/Downloads/dockeralex"
}
```

Despite the method you have to reload configuration and restart Docker:

```
sudo systemctl daemon-reload
sudo systemctl restart docker
```

To confirm that Docker was reconfigured:



```
docker info|grep "Docker Root Dir"
 Docker Root Dir: /home/madon/Downloads/dockeralex
```

https://github.com/IronicBadger/til/blob/master/docker/change-docker-root.md

```
rsync -a /var/lib/docker/* /home/madon/Downloads/dockeralex
```




madon@hp:~/minimalgcpcloudrunwsgi$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
myimage      latest    c03f4a577373   9 seconds ago    877MB
<none>       <none>    e295e2da8128   32 minutes ago   877MB
python       3.7       ac9dead5ba6f   36 hours ago     876MB

madon@hp:~/minimalgcpcloudrunwsgi$ docker rm e295e2da8128
Error: No such container: e295e2da8128


madon@hp:~/minimalgcpcloudrunwsgi$ docker image rm e295e2da8128
Error response from daemon: conflict: unable to delete e295e2da8128 (must be forced) - image is being used by stopped container a8331b483526



https://stackoverflow.com/questions/51188657/image-is-being-used-by-stopped-container/51189547

adon@hp:~$ docker ps -q -a
a8331b483526
madon@hp:~$ docker ps 
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
madon@hp:~$ docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                     PORTS     NAMES
a8331b483526   e295e2da8128   "python app/minimal_…"   4 minutes ago   Exited (2) 4 minutes ago             goofy_feistel


madon@hp:~$ docker rm a8331b483526
a8331b483526


madon@hp:~$  docker image rm e295e2da8128
Deleted: sha256:e295e2da8128b2c56c2905bea4f72357b0010a0c010cd030e41e6696b6343117
Deleted: sha256:3170568133b0d508e2d08eefc1753aa48480e35f20226f79b08fb067b0fab1e1
Deleted: sha256:3b4a31f94b69394bdc2e61ea4b8578629af706b51f9174f3fa5d30c1f674fb43
Deleted: sha256:996e8f6110dccf3ad26dd274d6201028cb4a6b83617ddd15d3d4f1fa205c86e5
Deleted: sha256:796224e07d8005c0f513727d5e0c5f229c3d2c55236c611bdb8015f8140c4cba
Deleted: sha256:6091b470f77a8b92cc1ad325631541e58796f3e7abe27ec4ff111526ea6f3334



enter a container:

docker ps
docker exec -it <container name> /bin/bash

If you want stdin:


```
docker run -it -p 8080:8080 myimage
```

```
docker run -it myimage
```



https://stackoverflow.com/questions/48368411/what-is-docker-run-it-flag






```
madon@hp:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS      NAMES
f67b5fc382f0   myimage   "python minimal_webs…"   34 seconds ago   Up 32 seconds   8080/tcp   busy_ardinghelli

madon@hp:~$ docker exec -it f67b5fc382f0 /bin/bash
root@f67b5fc382f0:/# ls
Dockerfile  boot  home	 media		       opt   run   sys	var
README.md   dev   lib	 minimal_webserver.py  proc  sbin  tmp
bin	    etc   lib64  mnt		       root  srv   usr

root@f67b5fc382f0:/# ps
  PID TTY          TIME CMD
    7 pts/1    00:00:00 bash
   14 pts/1    00:00:00 ps

root@f67b5fc382f0:/# ps auxf
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         7  0.2  0.0   5752  3660 pts/1    Ss   08:58   0:00 /bin/bash
root        16  0.0  0.0   9392  3132 pts/1    R+   08:59   0:00  \_ ps auxf
root         1  0.4  0.1  27280 19524 pts/0    Ss+  08:57   0:00 python minimal_
root@f67b5fc382f0:/# 
```




https://cloud.google.com/run/docs/logging




# Build the Docker File


```
docker build . -t [eu.]gcr.io/<PROJECT-ID>/<IMAGE-ID>

```

```
docker build . -t eu.gcr.io/photos-307521/myimage
```


```
madon@hp:~/minimalgcpcloudrunwsgi$ docker build . -t eu.gcr.io/photos-307521/myimage
Sending build context to Docker daemon  60.93kB
Step 1/5 : FROM python:3.7
 ---> ac9dead5ba6f
Step 2/5 : WORKDIR /
 ---> Using cache
 ---> 59b60f5a1710
Step 3/5 : COPY . /
 ---> 2821985c406b
Step 4/5 : EXPOSE 8080
 ---> Running in 81c1fd3b7670
Removing intermediate container 81c1fd3b7670
 ---> 474398dc8fb6
Step 5/5 : CMD ["python", "minimal_webserver.py"]
 ---> Running in bbecf2de240b
Removing intermediate container bbecf2de240b
 ---> f2ff700ec9be
Successfully built f2ff700ec9be
Successfully tagged eu.gcr.io/photos-307521/myimage:latest
```

# Test the Docker Build


docker run -p PORT:PORT eu.gcr.io/photos-307521/myimage


docker run eu.gcr.io/photos-307521/myimage

```
docker run -it eu.gcr.io/photos-307521/myimage
Serving on port 8080
```

# Push the Docker File to GCP

docker push eu.gcr.io/photos-307521/myimage


```
madon@hp:~/minimalgcpcloudrunwsgi$ docker push eu.gcr.io/photos-307521/myimage
Using default tag: latest
The push refers to repository [eu.gcr.io/photos-307521/myimage]
78f81059a26b: Retrying in 1 second 
0b18c63fe124: Retrying in 1 second 
abb35d8edc01: Retrying in 2 seconds 
2cdb72475c99: Retrying in 1 second 
04d1717d0e01: Retrying in 1 second 
dacb447ffe30: Waiting 
bde301416dd2: Waiting 
81496d8c72c2: Waiting 
644448d6e877: Waiting 
0e41e5bdb921: Waiting 
unknown: Service 'containerregistry.googleapis.com' is not enabled for consumer 'project:photos-307521'.
```


gcloud services enable containerregistry.googleapis.com 
or using console





madon@hp:~/minimalgcpcloudrunwsgi$ docker push eu.gcr.io/photos-307521/myimage
Using default tag: latest
The push refers to repository [eu.gcr.io/photos-307521/myimage]
78f81059a26b: Retrying in 1 second 
0b18c63fe124: Preparing 
abb35d8edc01: Preparing 
2cdb72475c99: Preparing 
04d1717d0e01: Retrying in 1 second 
dacb447ffe30: Waiting 
bde301416dd2: Waiting 
81496d8c72c2: Waiting 
644448d6e877: Waiting 
0e41e5bdb921: Waiting 
unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials. To authenticate your request, follow the steps in: https://cloud.google.com/container-registry/docs/advanced-authentication
m




cat keyfile.json | docker login -u _json_key --password-stdin https://eu.gcr.io

cat /home/madon/googledrivekey/photos-307521-596209aeaea4.json  | docker login -u _json_key --password-stdin https://eu.gcr.io


madon@hp:~/minimalgcpcloudrunwsgi$ cat /home/madon/googledrivekey/photos-307521-596209aeaea4.json  | docker login -u _json_key --password-stdin https://eu.gcr.io
WARNING! Your password will be stored unencrypted in /home/madon/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded


madon@hp:~/minimalgcpcloudrunwsgi$ docker push eu.gcr.io/photos-307521/myimage
Using default tag: latest
The push refers to repository [eu.gcr.io/photos-307521/myimage]
78f81059a26b: Pushed 
0b18c63fe124: Layer already exists 
abb35d8edc01: Layer already exists 
2cdb72475c99: Layer already exists 
04d1717d0e01: Layer already exists 
dacb447ffe30: Layer already exists 
bde301416dd2: Layer already exists 
81496d8c72c2: Layer already exists 
644448d6e877: Layer already exists 
0e41e5bdb921: Layer already exists 
latest: digest: sha256:3a96fe9beaea77fd0198d0f03a3dab6c64081c3c039e66d976b2e4eb914579d3 size: 2426



# Create Cloud Run Service

First, on your projects dashboard click Cloud Run on the left-hand side.

https://console.cloud.google.com/run?authuser=1&project=photos-307521

Then click ‘Create Service’, select the Container Image URL, choose the region (at the time of writing the only EU option is Belgium), Authentication (here set to Allow unauthenticated users), and optional settings. Note, it is important you select the appropriate port specified in main.py (here 8000). Next click ‘Create’ and your app will be created.

alexphotos

alexphotos Region: europe-west1 URL: https://alexphotos-vp2uadxsla-ew.a.run.app 


# dns

https://cloud.google.com/run/docs/mapping-custom-domains

photos.madon.net
A 	216.239.32.21
A 	216.239.34.21
A 	216.239.36.21
A 	216.239.38.21
AAAA 	2001:4860:4802:32::15
AAAA 	2001:4860:4802:34::15
AAAA 	2001:4860:4802:36::15
AAAA 	2001:4860:4802:38::15
	
