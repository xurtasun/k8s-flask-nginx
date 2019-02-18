Python APP with flask & uWSGI and nginx 
# Python APP with flask & uWSGI and nginx 
Este proyecto esta basado en una aplicación en python con Flask que muestra la hora actual.

Existen dos contenedores:
 - Python & Nginx (./Dockerfile)
 - Nginx Reverse Proxy (./proxy/Dockerfile)

Se ha configurado un Nginx que hace de reverse proxy y mantiene en cache durante 1 minuto el resultado.

En el path ./k8s/ estan los ficheros utilizados para el deployment en kubernetes.
  - ingress.yml	
  - nginx-rpc.yml
  - nginx-svc.yml	
  - python-app-rpc.yml
  - python-app-svc.yml
  
Se ha usado un replication controller para levantar 3 replicas de la Aplicación y 1 servicio para publicarla, un replicaController para hacer el reverse proxy con nginx hacia las replicas del aplicativo, el servicio de éste en modo NodePort (Inicialmente el servicio definido con LoadBalancer para publicar el servicio al exterior) para que el ingressController pueda redirigir el trafico hacia el servicio de reverse proxy.

