# Kubernetes YAML Configurations

## Certified Kubernetes Application Developer (CKAD) Practice Files

This repository contains YAML configuration files used to practice key Kubernetes concepts as part of the **Certified Kubernetes Application Developer (CKAD)** exam preparation.

## Structure

- `basic.yaml`: Pod definition using the NGINX image.
- `service.yaml`: Service definition to expose the NGINX Pod.
- `dashboard-adminuser.yaml`: ServiceAccount for Dashboard access.
- `dashboard-adminuser-role.yaml`: ClusterRoleBinding for admin Dashboard access.
- `dashboard-token-secret.yaml`: Secret token configuration for Dashboard login.

## Usage

Apply any configuration file:

```bash
kubectl apply -f <filename>.yaml
```



## Delete a configuration
``` bash
kubectl delete -f <filename>.yaml
```
## Dashboard Access
### Start the Kubernetes Dashboard
``` bash
microk8s dashboard-proxy
```
## Then open the following URL in your browser:

```cpp
https://127.0.0.1:10443
```
## Log in using the token provided in the terminal after running the proxy command.








