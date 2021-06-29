#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print("Access-Control-Allow-Origin: *")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")
cmd1=[]
cmd1=cmd.split()


if cmd1[0]=="create":
  print(subprocess.getoutput("sudo "+ "kubectl create deployment "+cmd1[-1]+ " --image=centos:8" +" --kubeconfig admin.conf"))
elif cmd1[0]=="delete":
  print(subprocess.getoutput("sudo "+ "kubectl delete deployment "+cmd1[-1]+" --kubeconfig admin.conf"))
elif cmd1[0]=="show":
  print(subprocess.getoutput("sudo "+ "kubectl describe pod "+cmd1[-1]+" --kubeconfig admin.conf"))
elif cmd1[0]=="get":
  print(subprocess.getoutput("sudo "+ "kubectl get pods"+" --kubeconfig admin.conf"))
elif cmd1[0]=="replicate":
  print(subprocess.getoutput("sudo "+ "kubectl scale deployment "+cmd1[1]+ " --replicas="+cmd1[-2]+" --kubeconfig admin.conf"))
elif cmd1[0]=="expose":
  print(subprocess.getoutput("sudo "+ "kubectl expose deployment "+cmd1[-1]+" --port=80 --type=NodePort --kubeconfig admin.conf"))
elif "services" in cmd1:
  print(subprocess.getoutput("sudo "+ "kubectl get svc --kubeconfig admin.conf"))
elif cmd1[0]=="remove":
 print(subprocess.getoutput("sudo "+ "kubectl delete svc "+cmd1[-1]+" --kubeconfig admin.conf"))