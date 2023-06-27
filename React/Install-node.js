<!-- Load React. -->
<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>

<!-- BABEL -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

CREATE REACT APP COMMAND-go to project dir:

1. This will install NPM(node package manager) locally.
install: sudo npm i -g create-react-app "create folder"->react-app will be created inside of the folder-name could be anything

2. This will install NPX(node package execute)-it will grab the modules/application from repo(better way).
install: npx create-react-app "create-folder"->react-app will be created inside of the folder-name could be anything

Node.js Current:
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt install nodejs

Node.js LTS:
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
