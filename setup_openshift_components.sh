#!/bin/sh

# Setup openshift namespaces, network policies and builds

oc apply -f - <<EOF
apiVersion: v1
kind: Namespace
metadata:
  name: nl-customer 
  annotations:
    openshift.io/node-selector: ""
  labels:
    name: nl-customer 
EOF


oc apply -f - <<EOF
apiVersion: v1
kind: Namespace
metadata:
  name: ie-customer 
  annotations:
    openshift.io/node-selector: ""
  labels:
    name: ie-customer 
EOF


# Create default network policies for multi-tenancy

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: allow-from-openshift-ingress
    namespace: nl-customer
spec:
    podSelector: {}
    ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            network.openshift.io/policy-group: ingress
    policyTypes:
    - Ingress
EOF

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: allow-from-self
    namespace: nl-customer
spec:
    podSelector:
    ingress:
    - from:
      - podSelector: {}
EOF

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: deny-by-default
    namespace: nl-customer
spec:
    podSelector:
    ingress: []
EOF

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: allow-from-openshift-ingress
    namespace: ie-customer
spec:
    podSelector: {}
    ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            network.openshift.io/policy-group: ingress
    policyTypes:
    - Ingress
EOF

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: allow-from-self
    namespace: ie-customer
spec:
    podSelector:
    ingress:
    - from:
      - podSelector: {}
EOF

oc apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
    name: deny-by-default
    namespace: ie-customer
spec:
    podSelector:
    ingress: []
EOF


#TODO: specific network policies
# PE namespace
# Builds and deployments
# Envoy config and deployments