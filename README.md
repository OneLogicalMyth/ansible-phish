# Ansible Phish
I wanted to learn Ansible so built a playbook for deploying a Digital Ocean phishing server for engagements.

It isn't perfect but for myself it appears to work very well.


# Installing Ansible
I use the Windows 10 Subsystem for Linux just for ease of use. So these instructions are based on the fact you have downloaded the Ubuntu 16 LTS from the Microsoft Store.

1. Open a bash prompt (from start menu, type 'bash' and hit enter).
2. Install Pip: `sudo apt-get -y install python-pip python-dev libffi-dev libssl-dev`
3. Upgrade Pip: `sudo pip install --upgrade pip`
4. Install Ansible: `pip install ansible --user`
    * _`--user` installs packages local to the user account instead of globally to avoid permissions issues with Pip and the Linux Subsystem_
5. Since the `ansible*` commands are installed under `~/.local/bin`, we need to add that to the $PATH, so run the command: `echo 'PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc`
6. Either exit out of the bash prompt and start it again from the Windows menu, or run `source .bashrc` to update your $PATH to include Ansible.

I took these instructions from [Jeff Geerling's Blog Post](https://www.jeffgeerling.com/blog/2017/using-ansible-through-windows-10s-subsystem-linux).


# Domain Configuration
Ensure that your domain you wish to use for the phish server has been purchased and the name servers set to use Digital Oceans prior to running the playbook. No other domain configuration is needed.


# Running the Playbook
1. Change the working directory to the root of the Git repositry
2. Edit the `vars/all` file
2. Start the deployment with `ansible-playbook DO_Phish.yml`

**NOTE: *Should the playbook fail, ensure you delete the domain name from digital ocean manually, there is currently no check to stop duplicate DNS records***
