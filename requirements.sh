# Simple modification of the installation file requirements.sh

function install() {
   clear
   echo -e "\033[32m[~] Updating packages..."
   apt update

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
       echo -e "\033[32m\n[~] Python3 is already installed."
   else
       echo -e "\033[31m\n[!] Python3 is not installed."
       sleep 2
       echo -e "\033[32m\n[~] Installing Python3..."
       apt install python3 -y
   fi

   echo -e "\033[32m\nInstalling requirements...\n"
   pip3 install -r requirements.txt
   
   echo -e "\n\033[32m[✔] Installation completed."
   echo -e "\n[~] Use the command: python3 ipscn.py to start the tool."
}

install