
#Docker backup script

#Reads docker ps command and creates a dict with container names and ID's

command = 'docker ps  --format "{{.ID}} {{.Names}}"'


#Removes any entry in dict that matches blacklist by key/name

#Reads docker volume ls and compares white list to remove as well

#docker commit -p <CONTAINER_ID> <BACKUP_NAME>
#docker backup volume something
