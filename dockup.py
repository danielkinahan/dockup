import subprocess
from datetime import date

#Docker backup script

backup_dir = "/home/daniel/.docker_backup_staging/"

docker_ps = ["docker", "ps", "--format", '"{{.ID}} {{.Names}}"']
#Reads docker ps command and creates a dict with container names and ID's

container_list = subprocess.run(docker_ps, capture_output=True)

for item in container_list.stdout.decode("utf-8").split("\n")[:-1]:
    item = item[1:-1]
    container_id, container_name = item.split(" ")

    backup_name = "backup" + str(date.today()) + container_name
    docker_commit = ["docker", "commit", "-p", container_id, backup_name]
    #commit_return = subprocess.run(docker_commit, capture_output=True)
    print(" ".join(docker_commit))

    backup_tar = backup_dir + backup_name + ".tar"
    docker_save = ["docker", "save", "-o", backup_tar, backup_name]
    print(" ".join(docker_save))
    #save_return = subprocess.run(docker_save, capture_output=True)

    docker_image_rm = ["docker", "image", "rm", backup_name]
    #docker_image_rm_return = subprocess.run(docker_image_rm, capture_output=True)
    print(" ".join(docker_image_rm))

#Reads docker volume ls and compares white list to remove as well

#docker commit -p <CONTAINER_ID> <BACKUP_NAME>
#docker backup volume something
