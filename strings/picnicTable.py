def printPicnic(itemDict, leftWidth, rightWidth):
  print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
  
  for k, v in itemDict.items():
    print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
  
  
picnicItems = {
  'sandwiches': 4,
  'apples': 12,
  'cups':4,
  'cookies': 8000
}

printPicnic(picnicItems, 12, 5)


# devops = devops engineer


# software developers --> code ---> operations -- automate --> CI/CD pipelines (python) --> Azure Cloud (vms) ---> Access

# compter (create website) ---> powerful comouter (create)


# chatgpt --> Agentic AI (software) --> RAG

# python
# git - version tracking


# devops
# AIOps

# Linux, bash
# Netwroking (http, json, rest api)
# git
# python
# database

# vector databse


# docker
# kubernetes
# terraform
# observability - monitor, logging, tracing