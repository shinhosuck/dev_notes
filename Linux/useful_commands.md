
# COPY FOLDER TO EXTERNAL DRIVE FOLDER:
cp -R 'folder name' /media/anderson/'WD Easystore'/'new folder name'

# CURRENT DIRECTORY:
pwd

# CREATE FOLDER:
mkdir 'folder name'

# CREATE TEXT FILE:
touch 'file.name' -> create a file
cat > file.name -> open the file
control + d -> ends the writting

# INSTALL VENV
sudo apt install python3-venv 

# CREATE PYTHON VIRTUAL ENVIRONMENT
python3 -m venv venv 

# DELETE TEXT FILE 
sudo rm -r sample.txt 

# DELETE FOLDER 
sudo rm -rf sample_folder

# NEW WINDOW TO OPEN IN THE MIDDLE OF THE SCREEN
gsettings set org.gnome.mutter center-new-windows true
gsettings set org.gnome.mutter center-new-windows false

# PLACE TRASH CAN ON THE WINDOW
gsettings set org.gnome.shell.extensions.ding show-trash true
gsettings set org.gnome.shell.extensions.ding show-trash false

# REFRESH SNAP STORE
snap-store --quit && sudo snap refresh snap-store
Or
killall snap-store
sudo snap refresh

# SCREEN DIM ISSUE-set it in the grub
acpi_backlight=vendor

# SEARCH IN THE TERMINAL
 - -iname => case insensitive
 - -name => case sensitive
find -iname "file or folder name'

# Remove apt lists and update => useful when there is a bad header
sudo rm -rf /var/lib/apt/lists/* && sudo apt-get update

# Disable snap auto refresh:
snap refresh --hold -> all snap
snap refresh --hold=24h firefox -> per snap app for period of time

# Unable snap auto refresh
snap refresh --unhold
snap refresh --unhold firefox -> per snap app















