1- sudo apt update
2- sudo apt install -y libfontconfig1 libcairo2 libjpeg-turbo8
3- sudo apt apt --fix-broken install
4- wget https://github.com/pdf2htmlEX/pdf2htmlEX/releases/download/v0.18.8.rc1/pdf2htmlEX-0.18.8.rc1-master-20200630-Ubuntu-bionic-x86_64.deb
5- sudo mv pdf2htmlEX-0.18.8.rc1-master-20200630-Ubuntu-bionic-x86_64.deb pdf2htmlEX.deb
6- sudo apt install ./pdf2htmlEX.deb
7- finally check the installation : pdf2htmlEX -v
