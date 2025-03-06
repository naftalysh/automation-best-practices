
# Best Free Books and Knowledge Sites for Learning Jenkins

## Free Books
1. **[Jenkins User Handbook](https://www.jenkins.io/doc/book/using/)** - Official Jenkins documentation that covers installation, usage, pipelines, and more. This is a great resource for both beginners and advanced users.
2. **[The Jenkins 2.x Cookbook](https://www.packtpub.com/free-ebooks)** - Available for free on certain days from Packt. It provides practical solutions to common Jenkins problems.
3. **[Getting Started with Jenkins](https://resources.jetbrains.com/storage/products/teamcity/pdf/TeamCity-vs-Jenkins.pdf)** - While this compares Jenkins with TeamCity, it offers a solid overview of Jenkins concepts.

## Knowledge Sites
1. **[Jenkins Official Documentation](https://www.jenkins.io/doc/)** - Comprehensive documentation on everything Jenkins, from installation to advanced configuration and plugins.
2. **[Jenkins Pipeline Tutorial by Baeldung](https://www.baeldung.com/jenkins-pipeline)** - An excellent tutorial on building Jenkins pipelines with examples.
3. **[DigitalOcean Community Tutorials](https://www.digitalocean.com/community/tutorials)** - Search for Jenkins-related tutorials here. DigitalOcean has many detailed guides on Jenkins setup, pipelines, and integrations.
4. **[Jenkins CI Blog](https://www.jenkins.io/blog/)** - Stay updated with the latest Jenkins news, tutorials, and best practices directly from the Jenkins community.
5. **[GitHub - Jenkins Example Pipelines](https://github.com/jenkinsci/pipeline-examples)** - A collection of example Jenkins pipelines that can be directly used or adapted for your projects.

## Running Jenkins
1. **[Docker/Podman (Linux/Windows)]()** - Run Jenkins with Podman
    ```sh
        podman run -d \
        --name jenkins \
        -p 8080:8080 -p 50000:50000 \
        -v jenkins_home:/var/jenkins_home \
        jenkins/jenkins:lts
    ```

    Or
    ```sh
        podman run -d \
        --pull=always \
        --name jenkins \
        -p 8080:8080 -p 50000:50000 \
        -v jenkins_home:/var/jenkins_home \
        docker.io/jenkins/jenkins:lts
    ```

  
2. **[Access the Jenkins Web Interface)](http://localhost:8080)** - 
3. **[Find the Initial Admin Password]()**    
    When Jenkins starts for the first time, it generates a default admin password. To retrieve it, you need to check the contents of the secrets/initialAdminPassword file inside the Jenkins container.
    
    You can retrieve the password using the following command:
    ```sh
        podman exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
    ``` 
    This command will print the initial admin password to the console.

4. **[Log In to Jenkins]()**
   * On the Jenkins web interface, you will be prompted to enter the initial admin password.
   * Paste the password retrieved from the previous step.
   * Click "Continue."

5. **[Set Up Your Jenkins Instance]()**
   After logging in, you will be guided through the initial setup process, where you can:
   * Install suggested plugins.
   * Create the first admin user (with your chosen username and password).
   * Customize the Jenkins instance.

6. **[Miscelanuous]()**
   * Find jenkins_home mount point (path)
   ```sh
   docker inspect jenkins | grep -i jenkins_home

   -->  "Name": "jenkins_home",
        "Source": "/home/nafta/.local/share/containers/storage/volumes/jenkins_home/_data",
   ```
   * Comment: Your current setup with the mounted volume will ensure that all Jenkins data is persistent across multiple Jenkins bootstraps. You don’t need to worry about data loss when stopping or restarting the Jenkins container. 

7. **[Stop and Remove the Jenkins Container]()**
   ```sh
   podman stop jenkins && podman rm jenkins && podman ps -a
   ```


