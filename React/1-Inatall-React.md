<!-- INSTALL REACT -->

<!-- Note: when deploying, replace "development.js" with "production.min.js". -->
<script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>

<!-- BABEL -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<!-- This will install NPM(node package manager) locally. -->
install: sudo npm i -g create-react-app "create folder"->react-app will be created inside of the folder-name could be anything

<!-- NODE JS CURRENT: -->
curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -
sudo apt install nodejs

<!-- NODE JS LTS: -->
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs

<!-- This will install NPX(node package execute)-it will grab the modules/application from repo(better way). -->
install: npx create-react-app "create-folder"->react-app will be created inside of the "create-folder"-name could be anything

<!-- Install react-router-dom -->
npm install react-router-dom
