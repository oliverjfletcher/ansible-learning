# Ansible Learning

Repository for work completed during course on Udemy called [Mastering Ansible](https://www.udemy.com/course/mastering-ansible)

## Vagrant Install Steps

`brew install virtualbox`

`brew install vagrant`

`vagrant plugin install vagrant-hostmanager`

`vagrant up`

## Ansible Install Steps

`sudo apt-get git`

`git config --global credential.helper store`

`pip install virtualenv`

`cd ansible-learning`

`virtualenv venv`

`source venv/bin/activate`

`pip3 install ansible`

`pip3 install ansible-lint`

## Ansible Vault Configuration

`ansible-vault create vault`

`echo "VAULT-PW" > ~/.vault_watchword.txt`

`chmod 0600 ~/.vault_watchword.txt`

## Ansible Commands

`ansible-playbook site.yml --list-tasks`

`ansible-playbook site.yml --start-at-task="install packages"`

`ansible-playbook playbook.yml --step`

`ansible-playbook --syntax-check site.yml`

`ansible-playbook --check`

## Links

- [Vagrant Image](https://app.vagrantup.com/ubuntu/boxes/bionic64)
- [Ansible Documentation](https://docs.ansible.com/ansible/2.9/index.html)
- [Module Index](https://docs.ansible.com/ansible/2.9/modules/modules_by_category.html)

